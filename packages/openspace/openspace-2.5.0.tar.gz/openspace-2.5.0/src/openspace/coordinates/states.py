from math import asin, atan2, cos, sin, sqrt, tan
from typing import List

from openspace.bodies.celestial import Earth, Moon, Sun
from openspace.coordinates.positions import PositionConvert, SphericalPosition
from openspace.math.constants import BASE_IN_KILO
from openspace.math.functions import LegendrePolynomial
from openspace.math.linalg import Matrix3D, Vector3D, Vector6D
from openspace.time import Epoch


class State:
    def __init__(self, epoch: Epoch, r: Vector3D, v: Vector3D) -> None:
        """class used to perform operations for time-dependent states

        :param epoch: time for which the position and velocity are valid
        :type epoch: Epoch
        :param r: position of the state
        :type r: Vector3D
        :param v: velocity of the state
        :type v: Vector3D
        """
        #: time for which the position and velocity are valid
        self.epoch: Epoch = epoch.copy()

        #: position of the state
        self.position: Vector3D = r.copy()

        #: velocity of the state
        self.velocity: Vector3D = v.copy()

        #: state vector whose elements are equal to that of the position and velocity unpacked
        self.vector = Vector6D.from_position_and_velocity(self.position, self.velocity)

    def copy(self):
        """create a duplicate of the calling state"""
        return type(self)(self.epoch, self.position, self.velocity)

    def vector_list(self) -> List[Vector3D]:
        """create a list of the position and velocity vectors

        :return: list of indices 0 == position and 1 == velocity
        :rtype: List[Vector3D]
        """
        return [self.position, self.velocity]


class ITRF(State):
    def __init__(self, epoch: Epoch, r: Vector3D, v: Vector3D) -> None:
        """class used to perform operations and modeling in the International Terrestrial Reference Frame

        :param epoch: time for which the position and velocity are valid
        :type epoch: Epoch
        :param r: position of the state
        :type r: Vector3D
        :param v: velocity of the state
        :type v: Vector3D
        """
        super().__init__(epoch, r, v)

    @classmethod
    def from_fixed(cls, epoch: Epoch, r: Vector3D) -> "ITRF":
        """create an ITRF state from a position fixed to the Earth surface

        :param epoch: time for which the position and velocity are valid
        :type epoch: Epoch
        :param r: position of the state
        :type r: Vector3D
        :return: ITRF state with velocity vector == 0
        :rtype: ITRF
        """
        return cls(epoch, r, Vector3D(0, 0, 0))


class HCW(State):
    def __init__(self, epoch: Epoch, r: Vector3D, v: Vector3D) -> None:
        """class used to perform operations and modeling in the HCW Frame

        :param epoch: time for which the position and velocity are valid
        :type epoch: Epoch
        :param r: position of the state
        :type r: Vector3D
        :param v: velocity of the state
        :type v: Vector3D
        """
        super().__init__(epoch, r, v)

    @classmethod
    def from_state_vector(cls, state_vec: Vector6D) -> "HCW":
        """create a hill state of from a full state vector

        :param state_vec: 6-dimensional vector of position and velocity
        :type state_vec: Vector6D
        :return: HCW state with arbitrary epoch
        :rtype: HCW
        """
        return cls(
            Epoch(0),
            Vector3D(state_vec.x, state_vec.y, state_vec.z),
            Vector3D(state_vec.vx, state_vec.vy, state_vec.vz),
        )

    @staticmethod
    def frame_matrix(origin: "GCRF") -> Matrix3D:
        """create a radial, in-track, cross-track axes matrix

        :param origin: inertial state that acts as the origin for the RIC frame
        :type origin: GCRF
        :return: matrix with rows of radial, in-track, and cross-track
        :rtype: Matrix3D
        """
        r: Vector3D = origin.position.normalized()
        c: Vector3D = origin.position.cross(origin.velocity).normalized()
        i: Vector3D = c.cross(r)
        return Matrix3D(r, i, c)


class GCRF(State):
    def __init__(self, epoch: Epoch, r: Vector3D, v: Vector3D) -> None:
        """class used to perform operations and modeling in the Geocentric Celestial Reference Frame

        :param epoch: time for which the position and velocity are valid
        :type epoch: Epoch
        :param r: position of the state
        :type r: Vector3D
        :param v: velocity of the state
        :type v: Vector3D
        """
        super().__init__(epoch, r, v)

        #: acceleration due to thrust
        self.thrust: Vector3D = Vector3D(0, 0, 0)

        #: scalar used for srp acceleration calculations
        self.srp_scalar: float = 0

        #: boolean to determine if perturbations are modeled during propagation
        self.use_perturbations: bool = True

    def acceleration_from_gravity(self) -> Vector3D:
        """calculates the gravity due to a nonspherical earth

        :return: vector representing the acceleration due to gravity
        :rtype: Vector3D
        """
        ecef: Vector3D = PositionConvert.gcrf.to_itrf(self.position, self.epoch)
        sphr_pos: SphericalPosition = SphericalPosition.from_cartesian(ecef)
        p: List[List[float]] = LegendrePolynomial(sphr_pos.declination).p

        m: int = 0
        n: int = 2

        partial_r: float = 0
        partial_phi: float = 0
        partial_lamb: float = 0
        recip_r: float = 1 / self.position.magnitude()
        mu_over_r: float = Earth.MU * recip_r
        r_over_r: float = Earth.RADIUS * recip_r
        r_exponent: float = 0
        clam: float = 0
        slam: float = 0
        recip_root: float = 1 / sqrt(ecef.x * ecef.x + ecef.y * ecef.y)
        rz_over_root: float = ecef.z * recip_r * recip_r * recip_root
        while n < Earth.DEGREE_AND_ORDER:
            m = 0
            r_exponent = r_over_r**n
            while m <= n:
                clam = cos(m * sphr_pos.right_ascension)
                slam = sin(m * sphr_pos.right_ascension)
                partial_r += r_exponent * (n + 1) * p[n][m] * (Earth.C[n][m] * clam + Earth.S[n][m] * slam)
                partial_phi += (
                    r_exponent
                    * (p[n][m + 1] - m * tan(sphr_pos.declination) * p[n][m])
                    * (Earth.C[n][m] * clam + Earth.S[n][m] * slam)
                )
                partial_lamb += r_exponent * m * p[n][m] * (Earth.S[n][m] * clam - Earth.C[n][m] * slam)

                m += 1

            n += 1

        partial_r *= -recip_r * mu_over_r
        partial_phi *= mu_over_r
        partial_lamb *= mu_over_r

        return PositionConvert.itrf.to_gcrf(
            Vector3D(
                (recip_r * partial_r - rz_over_root * partial_phi) * ecef.x
                - (recip_root * recip_root * partial_lamb) * ecef.y,
                (recip_r * partial_r - rz_over_root * partial_phi) * ecef.y
                + (recip_root * recip_root * partial_lamb) * ecef.x,
                recip_r * partial_r * ecef.z + (1 / recip_root) * recip_r * recip_r * partial_phi,
            ),
            self.epoch,
        )

    def acceleration_from_earth(self) -> Vector3D:
        """calculate the acceleration on the state due to earth's gravity

        :return: vector representing the acceleration from earth
        :rtype: Vector3D
        """
        r_mag: float = self.position.magnitude()

        return self.position.scaled(-Earth.MU / (r_mag * r_mag * r_mag))

    def acceleration_from_moon(self) -> Vector3D:
        """calculate the acceleration on the state due to the moon

        :return: vector representing the acceleration from the moon
        :rtype: Vector3D
        """
        s: Vector3D = Moon.get_position(self.epoch)
        r: Vector3D = s.minus(self.position)
        r_mag: float = r.magnitude()
        s_mag: float = s.magnitude()
        vec_1: Vector3D = r.scaled(1 / (r_mag * r_mag * r_mag))
        vec_2: Vector3D = s.scaled(1 / (s_mag * s_mag * s_mag))
        return vec_1.minus(vec_2).scaled(Moon.MU)

    def acceleration_from_sun(self) -> Vector3D:
        """calculate the acceleration on the state due to the sun

        :return: vector representing the acceleration from the sun
        :rtype: Vector3D
        """
        s: Vector3D = Sun.get_position(self.epoch)
        r: Vector3D = s.minus(self.position)
        r_mag: float = r.magnitude()
        s_mag: float = s.magnitude()
        vec_1: Vector3D = r.scaled(1 / (r_mag * r_mag * r_mag))
        vec_2: Vector3D = s.scaled(1 / (s_mag * s_mag * s_mag))
        return vec_1.minus(vec_2).scaled(Sun.MU)

    def acceleration_from_srp(self) -> Vector3D:
        """calculate the acceleration on the state from solar radiation pressure

        :return: vector representing the acceleration from srp
        :rtype: Vector3D
        """
        sun_vec: Vector3D = self.sun_vector().normalized()
        s_mag: float = sun_vec.magnitude()
        return sun_vec.scaled(-Sun.P * self.srp_scalar / (s_mag * s_mag * BASE_IN_KILO))

    def acceleration_from_thrust(self) -> Vector3D:
        """retrieve the stored acceleration to be applied from thrusters

        :return: the current acceleration vector in the GCRF frame
        :rtype: Vector3D
        """
        return self.thrust.copy()

    def derivative(self) -> List[Vector3D]:
        """create a list with elements 0 == velocity and 1 == acceleration

        :return: list of velocity and acceleration
        :rtype: List[Vector3D]
        """
        net_a: Vector3D = self.acceleration_from_thrust()
        net_a = net_a.plus(self.acceleration_from_earth())
        if self.use_perturbations:
            net_a = net_a.plus(self.acceleration_from_moon())
            net_a = net_a.plus(self.acceleration_from_sun())
            net_a = net_a.plus(self.acceleration_from_srp())
            net_a = net_a.plus(self.acceleration_from_gravity())
        return [self.velocity.copy(), net_a]

    def sun_vector(self) -> Vector3D:
        """create a vector pointing from the calling state to the sun

        :return: vector originating at the calling state and terminating at the sun
        :rtype: Vector3D
        """
        return Sun.get_position(self.epoch).minus(self.position)

    def moon_vector(self) -> Vector3D:
        """create a vector pointing from the calling state to the moon

        :return: vector originating at the calling state and terminating at the moon
        :rtype: Vector3D
        """
        return Moon.get_position(self.epoch).minus(self.position)


class IJK(State):
    def __init__(self, epoch: Epoch, r: Vector3D, v: Vector3D) -> None:
        """class used to perform operations and modeling in the Geocentric Equatorial Coordinate System

        :param epoch: time for which the position and velocity are valid
        :type epoch: Epoch
        :param r: position of the state
        :type r: Vector3D
        :param v: velocity of the state
        :type v: Vector3D
        """
        super().__init__(epoch, r, v)


class _StateConvertGCRF:
    """class used to perform state conversions from GCRF"""

    @staticmethod
    def to_hcw(origin: GCRF, state: GCRF) -> HCW:
        """create a state in the HCW frame

        :param origin: state which represents the origin of the relative frame
        :type origin: GCRF
        :param state: state to be modeled in the Hill frame
        :type state: GCRF
        :return: HCW state
        :rtype: HCW
        """
        magrtgt: float = origin.position.magnitude()
        magrint: float = state.position.magnitude()
        rot_eci_rsw: Matrix3D = HCW.frame_matrix(origin)
        vtgtrsw: Vector3D = rot_eci_rsw.multiply_vector(origin.velocity)
        rintrsw: Vector3D = rot_eci_rsw.multiply_vector(state.position)
        vintrsw: Vector3D = rot_eci_rsw.multiply_vector(state.velocity)

        sinphiint: float = rintrsw.z / magrint
        phiint: float = asin(sinphiint)
        cosphiint: float = cos(phiint)
        lambdaint: float = atan2(rintrsw.y, rintrsw.x)
        sinlambdaint: float = sin(lambdaint)
        coslambdaint: float = cos(lambdaint)
        lambdadottgt: float = vtgtrsw.y / magrtgt

        r_hcw: Vector3D = Vector3D(magrint - magrtgt, lambdaint * magrtgt, phiint * magrtgt)

        rot_rsw_sez: Matrix3D = Matrix3D(
            Vector3D(sinphiint * coslambdaint, sinphiint * sinlambdaint, -cosphiint),
            Vector3D(-sinlambdaint, coslambdaint, 0),
            Vector3D(cosphiint * coslambdaint, cosphiint * sinlambdaint, sinphiint),
        )

        vintsez: Vector3D = rot_rsw_sez.multiply_vector(vintrsw)
        phidotint: float = -vintsez.x / magrint
        lambdadotint: float = vintsez.y / (magrint * cosphiint)

        v_hcw: Vector3D = Vector3D(
            vintsez.z - vtgtrsw.x,
            magrtgt * (lambdadotint - lambdadottgt),
            magrtgt * phidotint,
        )

        return HCW(origin.epoch, r_hcw, v_hcw)


class _StateConvertHCW:
    """class used to perform conversions from the Hill frame"""

    @staticmethod
    def to_gcrf(state: HCW, origin: GCRF) -> GCRF:
        """create an inertial state for the calling state

        :param origin: inertial state that acts as the origin for the relative state
        :type origin: GCRF
        :return: inertial state of the relative spacecraft
        :rtype: GCRF
        """
        magrtgt: float = origin.position.magnitude()
        magrint: float = magrtgt + state.position.x
        rot_eci_rsw: Matrix3D = HCW.frame_matrix(origin)
        vtgtrsw: Vector3D = rot_eci_rsw.multiply_vector(origin.velocity)

        lambdadottgt: float = vtgtrsw.y / magrtgt
        lambdaint: float = state.position.y / magrtgt
        phiint: float = state.position.z / magrtgt
        sinphiint: float = sin(phiint)
        cosphiint: float = cos(phiint)
        sinlambdaint: float = sin(lambdaint)
        coslambdaint: float = cos(lambdaint)

        rot_rsw_sez: Matrix3D = Matrix3D(
            Vector3D(sinphiint * coslambdaint, sinphiint * sinlambdaint, -cosphiint),
            Vector3D(-sinlambdaint, coslambdaint, 0),
            Vector3D(cosphiint * coslambdaint, cosphiint * sinlambdaint, sinphiint),
        )

        rdotint: float = state.velocity.x + vtgtrsw.x
        lambdadotint: float = state.velocity.y / magrtgt + lambdadottgt
        phidotint: float = state.velocity.z / magrtgt
        vintsez: Vector3D = Vector3D(-magrint * phidotint, magrint * lambdadotint * cosphiint, rdotint)
        vintrsw: Vector3D = rot_rsw_sez.transpose().multiply_vector(vintsez)
        vinteci: Vector3D = rot_eci_rsw.transpose().multiply_vector(vintrsw)

        rintrsw: Vector3D = Vector3D(
            cosphiint * magrint * coslambdaint,
            cosphiint * magrint * sinlambdaint,
            sinphiint * magrint,
        )

        rinteci: Vector3D = rot_eci_rsw.transpose().multiply_vector(rintrsw)

        return GCRF(origin.epoch, rinteci, vinteci)


class StateConvert:
    """class used to perform state conversions"""

    #: used to convert from HCW to other frames
    hcw = _StateConvertHCW

    #: used to convert from GCRF to other frames
    gcrf = _StateConvertGCRF
