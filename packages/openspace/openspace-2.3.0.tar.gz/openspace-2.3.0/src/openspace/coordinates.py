from math import asin, atan2, cos, pi, radians, sin, sqrt, tan
from typing import List

from openspace.bodies.celestial import Earth, Moon, Sun
from openspace.math.functions import Conversions, LegendrePolynomial, sign
from openspace.math.linalg import Matrix3D, Vector3D, Vector6D
from openspace.time import Epoch


class HillState:
    def __init__(self, position: Vector3D, velocity: Vector3D) -> None:
        """used to perform relative motion operations for two spacecraft represented in the Hill frame

        :param position: relative position of the two spacecraft in km
        :type position: Vector3D
        :param velocity: relative velocity of the two spacecraft in km/s
        :type velocity: Vector3D
        """
        #: relative position of the two spacecraft in km
        self.position: Vector3D = position.copy()

        #: relative velocity of the two spacecraft in km/s
        self.velocity: Vector3D = velocity.copy()

        #: state vector whose elements are equal to that of the position and velocity unpacked
        self.vector = Vector6D.from_position_and_velocity(self.position, self.velocity)

    @classmethod
    def from_state_vector(cls, state: Vector6D) -> "HillState":
        """create a HillState from a 6-D state vector

        :param state: state vector with components of the position and velocity in km and km/s respectively
        :type state: Vector6D
        :return: the 6-D vector represented as a relative state object
        :rtype: HillState
        """
        return cls(Vector3D(state.x, state.y, state.z), Vector3D(state.vx, state.vy, state.vz))

    @classmethod
    def from_gcrf(cls, state: "GCRFstate", origin: "GCRFstate") -> "HillState":
        """create a relative state from two inertial states

        :param state: inertial state of the chase vehicle
        :type state: GCRFstate
        :param origin: inertial state that will act as the origin for the frame
        :type origin: GCRFstate
        :return: relative state of the two inertial states
        :rtype: HillState
        """
        magrtgt: float = origin.position.magnitude()
        magrint: float = state.position.magnitude()
        rot_eci_rsw: Matrix3D = HillState.frame_matrix(origin)
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

        rhill: Vector3D = Vector3D(magrint - magrtgt, lambdaint * magrtgt, phiint * magrtgt)

        rot_rsw_sez: Matrix3D = Matrix3D(
            Vector3D(sinphiint * coslambdaint, sinphiint * sinlambdaint, -cosphiint),
            Vector3D(-sinlambdaint, coslambdaint, 0),
            Vector3D(cosphiint * coslambdaint, cosphiint * sinlambdaint, sinphiint),
        )

        vintsez: Vector3D = rot_rsw_sez.multiply_vector(vintrsw)
        phidotint: float = -vintsez.x / magrint
        lambdadotint: float = vintsez.y / (magrint * cosphiint)

        vhill: Vector3D = Vector3D(
            vintsez.z - vtgtrsw.x,
            magrtgt * (lambdadotint - lambdadottgt),
            magrtgt * phidotint,
        )

        return cls(rhill, vhill)

    @staticmethod
    def frame_matrix(origin: "GCRFstate") -> Matrix3D:
        """create a radial, in-track, cross-track axes matrix

        :param origin: inertial state that acts as the origin for the RIC frame
        :type origin: GCRFstate
        :return: matrix with rows of radial, in-track, and cross-track
        :rtype: Matrix3D
        """
        r: Vector3D = origin.position.normalized()
        c: Vector3D = origin.position.cross(origin.velocity).normalized()
        i: Vector3D = c.cross(r)
        return Matrix3D(r, i, c)

    def copy(self) -> "HillState":
        """create a replica of the calling state

        :return: state with elements equal to that of the calling state
        :rtype: HillState
        """
        return HillState(self.position, self.velocity)

    def to_gcrf(self, origin: "GCRFstate") -> "GCRFstate":
        """create an inertial state for the calling state

        :param origin: inertial state that acts as the origin for the relative state
        :type origin: GCRFstate
        :return: inertial state of the relative spacecraft
        :rtype: GCRFstate
        """
        magrtgt: float = origin.position.magnitude()
        magrint: float = magrtgt + self.position.x
        rot_eci_rsw: Matrix3D = HillState.frame_matrix(origin)
        vtgtrsw: Vector3D = rot_eci_rsw.multiply_vector(origin.velocity)

        lambdadottgt: float = vtgtrsw.y / magrtgt
        lambdaint: float = self.position.y / magrtgt
        phiint: float = self.position.z / magrtgt
        sinphiint: float = sin(phiint)
        cosphiint: float = cos(phiint)
        sinlambdaint: float = sin(lambdaint)
        coslambdaint: float = cos(lambdaint)

        rot_rsw_sez: Matrix3D = Matrix3D(
            Vector3D(sinphiint * coslambdaint, sinphiint * sinlambdaint, -cosphiint),
            Vector3D(-sinlambdaint, coslambdaint, 0),
            Vector3D(cosphiint * coslambdaint, cosphiint * sinlambdaint, sinphiint),
        )

        rdotint: float = self.velocity.x + vtgtrsw.x
        lambdadotint: float = self.velocity.y / magrtgt + lambdadottgt
        phidotint: float = self.velocity.z / magrtgt
        vintsez: Vector3D = Vector3D(-magrint * phidotint, magrint * lambdadotint * cosphiint, rdotint)
        vintrsw: Vector3D = rot_rsw_sez.transpose().multiply_vector(vintsez)
        vinteci: Vector3D = rot_eci_rsw.transpose().multiply_vector(vintrsw)

        rintrsw: Vector3D = Vector3D(
            cosphiint * magrint * coslambdaint,
            cosphiint * magrint * sinlambdaint,
            sinphiint * magrint,
        )

        rinteci: Vector3D = rot_eci_rsw.transpose().multiply_vector(rintrsw)

        return GCRFstate(origin.epoch, rinteci, vinteci)


class GCRFstate:
    def __init__(self, epoch: Epoch, position: Vector3D, velocity: Vector3D) -> None:
        """used to perform operations in the ECI frame

        :param epoch: valid time of the state
        :type epoch: Epoch
        :param position: position of the inertial state in km
        :type position: Vector3D
        :param velocity: velocity of the inertial state in km/s
        :type velocity: Vector3D
        """
        #: valid time of the state
        self.epoch: Epoch = epoch.copy()

        #: position of the inertial state in km
        self.position: Vector3D = position.copy()

        #: velocity of the inertial state in km/s
        self.velocity: Vector3D = velocity.copy()

        #: acceleration due to thrust
        self.thrust: Vector3D = Vector3D(0, 0, 0)

    @classmethod
    def from_hill(cls, origin: "GCRFstate", state: HillState) -> "GCRFstate":
        """create an inertial state from a relative state

        :param origin: inertial state that acts as the origin for the relative system
        :type origin: GCRFstate
        :param state: relative state of the spacecraft
        :type state: HillState
        :return: inertial state of the spacecraft
        :rtype: GCRFstate
        """
        return state.to_gcrf(origin)

    def copy(self) -> "GCRFstate":
        """create a replica of the calling state

        :return: state with attributes equal to the calling state
        :rtype: GCRFstate
        """
        return GCRFstate(self.epoch, self.position, self.velocity)

    def vector_list(self) -> List[Vector3D]:
        """create a list with elements of 0 == position and 1 == velocity

        :return: list of position and velocity
        :rtype: List[Vector3D]
        """
        return [self.position.copy(), self.velocity.copy()]

    def acceleration_from_gravity(self) -> Vector3D:
        """calculates the gravity due to a nonspherical earth

        :return: vector representing the acceleration due to gravity
        :rtype: Vector3D
        """
        ecef: Vector3D = self.itrf_position()
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

        ecef_a: Vector3D = Vector3D(
            (recip_r * partial_r - rz_over_root * partial_phi) * ecef.x
            - (recip_root * recip_root * partial_lamb) * ecef.y,
            (recip_r * partial_r - rz_over_root * partial_phi) * ecef.y
            + (recip_root * recip_root * partial_lamb) * ecef.x,
            recip_r * partial_r * ecef.z + (1 / recip_root) * recip_r * recip_r * partial_phi,
        )

        return ITRFstate(self.epoch, ecef_a, Vector3D(0, 0, 0)).gcrf_position()

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
        return sun_vec.scaled(-Sun.P * 3.6e-5)

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
        net_0: Vector3D = self.acceleration_from_thrust()
        net_1: Vector3D = net_0.plus(self.acceleration_from_moon())
        net_2: Vector3D = net_1.plus(self.acceleration_from_sun())
        net_3: Vector3D = net_2.plus(self.acceleration_from_srp())
        net_4: Vector3D = net_3.plus(self.acceleration_from_gravity())
        net_a: Vector3D = net_4.plus(self.acceleration_from_earth())
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

    def itrf_position(self) -> Vector3D:
        """create a vector that represents the state's position in the earth-fixed frame

        :return: the position of the state in the itrf frame
        :rtype: Vector3D
        """
        mod: Vector3D = Precession.matrix(self.epoch).multiply_vector(self.position)
        tod: Vector3D = Nutation.matrix(self.epoch).multiply_vector(mod)
        return Rotation.matrix(self.epoch).multiply_vector(tod)


class Rotation:
    """class used to transform between itrf and tod

    :return: defined in static methods
    :rtype: defined in static methods
    """

    @staticmethod
    def matrix(epoch: Epoch) -> Matrix3D:
        """creates a matrix that can be used to transform an itrf position to tod and vice versa

        :param epoch: valid time of the state
        :type epoch: Epoch
        :return: transformation matrix
        :rtype: Matrix3D
        """
        d: float = epoch.julian_value() - Epoch.J2000_JULIAN_DATE
        arg1: float = radians(125.0 - 0.05295 * d)
        arg2: float = radians(200.9 + 1.97129 * d)
        a: float = radians(-0.0048)
        b: float = radians(0.0004)
        dpsi: float = a * sin(arg1) - b * sin(arg2)
        eps: float = Earth.obliquity_of_ecliptic_at_epoch(epoch)
        gmst: float = epoch.greenwich_hour_angle()
        gast: float = dpsi * cos(eps) + gmst
        return Vector3D.rotation_matrix(Vector3D(0, 0, 1), -gast)


class Precession:
    """class used to transform between tod and mod

    :return: defined in static methods
    :rtype: defined in static methods
    """

    @staticmethod
    def matrix(epoch: Epoch) -> Matrix3D:
        """creates a matrix that can be used to transform a tod position to mod and vice versa

        :param epoch: valid time of the state
        :type epoch: Epoch
        :return: transformation matrix
        :rtype: Matrix3D
        """
        t: float = epoch.julian_centuries_past_j2000()
        a: float = Conversions.dms_to_radians(0, 0, 2306.2181)
        b: float = Conversions.dms_to_radians(0, 0, 0.30188)
        c: float = Conversions.dms_to_radians(0, 0, 0.017998)
        x: float = a * t + b * t * t + c * t * t * t

        a = Conversions.dms_to_radians(0, 0, 2004.3109)
        b = Conversions.dms_to_radians(0, 0, 0.42665)
        c = Conversions.dms_to_radians(0, 0, 0.041833)
        y: float = a * t - b * t * t - c * t * t * t

        a = Conversions.dms_to_radians(0, 0, 0.7928)
        b = Conversions.dms_to_radians(0, 0, 0.000205)
        z: float = x + a * t * t + b * t * t * t

        sz = sin(z)
        sy = sin(y)
        sx = sin(x)
        cz = cos(z)
        cy = cos(y)
        cx = cos(x)

        return Matrix3D(
            Vector3D(-sz * sx + cz * cy * cx, -sz * cx - cz * cy * sx, -cz * sy),
            Vector3D(cz * sx + sz * cy * cx, cz * cx - sz * cy * sx, -sz * sy),
            Vector3D(sy * cx, -sy * sx, cy),
        )


class Nutation:
    """class used to transform between mod and gcrf

    :return: defined in static methods
    :rtype: defined in static methods
    """

    @staticmethod
    def matrix(epoch: Epoch) -> Matrix3D:
        """creates a matrix that can be used to transform a mod position to gcrf and vice versa

        :param epoch: valid time of the state
        :type epoch: Epoch
        :return: transformation matrix
        :rtype: Matrix3D
        """
        d = epoch.julian_value() - Epoch.J2000_JULIAN_DATE
        arg1 = radians(125.0 - 0.05295 * d)
        arg2 = radians(200.9 + 1.97129 * d)
        a = radians(-0.0048)
        b = radians(0.0004)
        dpsi = a * sin(arg1) - b * sin(arg2)
        a = radians(0.0026)
        b = radians(0.0002)
        deps = a * cos(arg1) + b * cos(arg2)
        eps = Earth.obliquity_of_ecliptic_at_epoch(epoch)

        ce = cos(eps)
        se = sin(eps)

        return Matrix3D(
            Vector3D(1.0, -dpsi * ce, -dpsi * se),
            Vector3D(dpsi * ce, 1.0, -deps),
            Vector3D(dpsi * se, deps, 1.0),
        )


class ITRFstate:
    def __init__(self, epoch: Epoch, position: Vector3D, velocity: Vector3D) -> None:
        """used to represent states in the earth-fixed frame

        :param epoch: valid time of the state
        :type epoch: Epoch
        :param position: position of the state in km
        :type position: Vector3D
        :param velocity: velocity of the state in km/s
        :type velocity: Vector3D
        """
        #: valid time of the state
        self.epoch: Epoch = epoch.copy()

        #: position of the state in km
        self.position: Vector3D = position.copy()

        #: velocity of the state in km/s
        self.velocity: Vector3D = velocity.copy()

    def copy(self) -> "ITRFstate":
        """create a duplicate state

        :return: copy of calling state
        :rtype: ITRFstate
        """
        return ITRFstate(self.epoch, self.position, self.velocity)

    def gcrf_state(self) -> GCRFstate:
        """calculate the inertial equivalent of the calling earth-fixed state

        :return: inertial representation of the calling state
        :rtype: GCRFstate
        """
        pos: Vector3D = self.gcrf_position()
        tod: Vector3D = Rotation.matrix(self.epoch).transpose().multiply_vector(self.velocity)
        mod: Vector3D = Nutation.matrix(self.epoch).transpose().multiply_vector(tod)
        vel: Vector3D = Precession.matrix(self.epoch).transpose().multiply_vector(mod)
        return GCRFstate(self.epoch, pos, vel)

    def gcrf_position(self) -> Vector3D:
        """create a vector that represents the position of the calling state in the inertial frame

        :return: ECI position of the calling state
        :rtype: Vector3D
        """
        tod: Vector3D = Rotation.matrix(self.epoch).transpose().multiply_vector(self.position)
        mod: Vector3D = Nutation.matrix(self.epoch).transpose().multiply_vector(tod)
        return Precession.matrix(self.epoch).transpose().multiply_vector(mod)

    def lla_state(self) -> "LLAstate":
        """calculate the latitude, longitude, and altitude of the ecf position

        :return: geodetic lat, long, altitude of the ecf position
        :rtype: LLAstate
        """
        pos: Vector3D = self.position
        x: float = pos.x
        y: float = pos.y
        z: float = pos.z

        # Equation 2.77a
        a: float = Earth.RADIUS
        a2: float = a * a
        f: float = Earth.FLATTENING
        b: float = a - f * a
        b2: float = b * b
        e2: float = 1 - b2 / a2
        eps2: float = a2 / b2 - 1.0
        rho: float = sqrt(x * x + y * y)

        # Equation 2.77b
        p: float = abs(z) / eps2
        s: float = rho * rho / (e2 * eps2)
        q: float = p * p - b2 + s

        # Equation 2.77c
        u: float = p / sqrt(q)
        v: float = b2 * u * u / q
        cap_p: float = 27.0 * v * s / q
        cap_q: float = (sqrt(cap_p + 1) + sqrt(cap_p)) ** (2.0 / 3.0)

        # Equation 2.77d
        t: float = (1.0 + cap_q + 1.0 / cap_q) / 6.0
        c: float = sqrt(u * u - 1.0 + 2.0 * t)
        w: float = (c - u) / 2.0

        # Equation 2.77e
        base: float = sqrt(t * t + v) - u * w - t / 2.0 - 0.25
        if base < 0:
            base = 0
        arg: float = w + sqrt(base)
        d: float = sign(z) * sqrt(q) * arg

        # Equation 2.77f
        n: float = a * sqrt(1.0 + eps2 * d * d / b2)
        arg = (eps2 + 1.0) * (d / n)
        lamb: float = asin(arg)

        # Equation 2.77g
        h: float = rho * cos(lamb) + z * sin(lamb) - a2 / n
        phi: float = atan2(y, x)
        if phi < 0:
            phi += pi * 2.0

        return LLAstate(lamb, phi, h)


class SphericalPosition:
    def __init__(self, r: float, ra: float, dec: float) -> None:
        """class used to perform spherical transformations

        :param r: magnitude of the vector
        :type r: float
        :param ra: right ascension of the vector (radians)
        :type ra: float
        :param dec: declination of the vector (radians)
        :type dec: float
        """
        #: magnitude of the vector
        self.radius: float = r

        #: right ascension of the vector in radians
        self.right_ascension: float = ra

        #: declination of the vector in radians
        self.declination: float = dec

    @classmethod
    def from_cartesian(cls, pos: Vector3D) -> "SphericalPosition":
        """create a spherical vector using cartesian components

        :param pos: cartesian vector
        :type pos: Vector3D
        :return: position represented with spherical components
        :rtype: SphericalPosition
        """
        ra: float = atan2(pos.y, pos.x)
        if ra < 0:
            ra += 2 * pi
        dec: float = atan2(pos.z, sqrt(pos.x * pos.x + pos.y * pos.y))
        return cls(pos.magnitude(), ra, dec)

    def to_cartesian(self) -> Vector3D:
        """calculate the vector as represented by x, y, and z

        :return: vector of equal magnitude in direction but in cartesian coordinates
        :rtype: Vector3D
        """
        cd: float = cos(self.declination)
        return Vector3D(cd * cos(self.right_ascension), cd * sin(self.right_ascension), sin(self.declination)).scaled(
            self.radius
        )


class LLAstate:
    def __init__(self, lat: float, longit: float, alt: float) -> None:
        """used to perform operations for a state in an oblate earth frame

        :param lat: geodetic latitude in radians
        :type lat: float
        :param long: geodetic longitude in radians
        :type long: float
        :param alt: altitude above the surface in km
        :type alt: float
        """
        #: geodetic latitude in radians
        self.latitude: float = lat

        #: geodetic longitude in radians
        self.longitude: float = longit

        #: altitude above the surface in km
        self.altitude: float = alt

    def copy(self) -> "LLAstate":
        """creates a duplicate of the calling state

        :return: state with properties that match that of the calling state
        :rtype: LLAstate
        """
        return LLAstate(self.latitude, self.longitude, self.altitude)

    def itrf_position(self) -> Vector3D:
        """creates a cartesian vector to represent the lat, long, and altitude

        :return: the earth-fixed cartesian position of the lat, long, and altitude
        :rtype: Vector3D
        """
        lat: float = self.latitude
        longitude: float = self.longitude
        alt: float = self.altitude

        f: float = Earth.FLATTENING
        e: float = sqrt(f * (2 - f))
        slat: float = sin(lat)
        clat: float = cos(lat)
        n: float = Earth.RADIUS / sqrt(1 - e * e * slat * slat)

        return Vector3D(
            (n + alt) * clat * cos(longitude), (n + alt) * clat * sin(longitude), (n * (1.0 - e * e) + alt) * slat
        )


class ClassicalElements:

    ECCENTRIC_ANOMALY_TOLERANCE: float = 1e-12

    def __init__(self, epoch: Epoch, a: float, e: float, i: float, raan: float, arg_per: float, ma: float) -> None:
        """used to perform calculations with the classical orbital elements

        :param epoch: epoch for which the elements are valid
        :type epoch: Epoch
        :param a: semi-major axis in km
        :type a: float
        :param e: eccentricity
        :type e: float
        :param i: inclination in radians
        :type i: float
        :param raan: right ascension of the ascending node in radians
        :type raan: float
        :param arg_per: argument of perigee in radians
        :type arg_per: float
        :param ma: mean anomaly in radians
        :type ma: float
        """
        #: epoch for which the element set is valid
        self.epoch: Epoch = epoch.copy()

        #: semi-major axis in km
        self.semimajor_axis: float = a

        #: eccentricity
        self.eccentricity: float = e

        #: inclination in radians
        self.inclination: float = i

        #: right ascension of the ascending node in radians
        self.raan: float = raan

        #: argument of perigee in radians
        self.argument_of_perigee: float = arg_per

        #: mean anomaly in radians
        self.mean_anomaly: float = ma

    @staticmethod
    def mean_anomaly_to_eccentric_anomaly(ma: float, e: float) -> float:
        """calculate the eccentric anomaly

        :param ma: mean anomaly in radians
        :type ma: float
        :param e: eccentricity
        :type e: float
        :return: eccentric anomaly in radians
        :rtype: float
        """
        converged: bool = False
        ea0: float = ma
        num: float
        den: float
        if e > 0.8:
            ea0 = pi
        while not converged:
            num = ma - ea0 + e * sin(ea0)
            den = 1 - e * cos(ea0)
            ean = ea0 + num / den
            if abs(ean - ea0) < ClassicalElements.ECCENTRIC_ANOMALY_TOLERANCE:
                converged = True
            else:
                ea0 = ean

        if ean < 0:
            ean += 2 * pi

        return ean

    @staticmethod
    def sma_from_r_and_v(r: float, v: float) -> float:
        """calculate the semi-major axis in km

        :param r: magnitude of the position vector in km
        :type r: float
        :param v: magnitude of the velocity vector in km/s
        :type v: float
        :return: semi-major axis in km
        :rtype: float
        """
        return 1 / (2 / r - v * v / Earth.MU)

    @staticmethod
    def mean_motion_from_sma(a: float) -> float:
        """calculate the mean motion

        :param a: semi-major axis in km
        :type a: float
        :return: mean motion in radians per second
        :rtype: float
        """
        return sqrt(Earth.MU / (a * a * a))

    @staticmethod
    def period_from_sma(a: float) -> float:
        """calculate the period

        :param a: semi-major axis in km
        :type a: float
        :return: period in seconds
        :rtype: float
        """
        return 2 * pi * sqrt((a * a * a) / Earth.MU)

    @staticmethod
    def areal_velocity_from_r_and_v(r: Vector3D, v: Vector3D) -> Vector3D:
        """calculate the momentum vector

        :param r: position vector in km
        :type r: Vector3D
        :param v: velocity vector in km/s
        :type v: Vector3D
        :return: areal velocity vector in km^2/s
        :rtype: Vector3D
        """
        return r.cross(v)

    @staticmethod
    def semilatus_rectum_from_h(h: float) -> float:
        """calculate the semi-latus rectum

        :param h: areal velocity magnitude
        :type h: float
        :return: semi-latus rectum in km
        :rtype: float
        """
        return h * h / Earth.MU

    @staticmethod
    def inclination_from_w(w: Vector3D) -> float:
        """calculate the inclination

        :param w: normalized momentum vector
        :type w: Vector3D
        :return: inclination in radians
        :rtype: float
        """
        i: float = atan2(sqrt(w.x * w.x + w.y * w.y), w.z)
        if i < 0:
            i += 2 * pi
        return atan2(sqrt(w.x * w.x + w.y * w.y), w.z)

    @staticmethod
    def eccentricity_from_p_and_a(p: float, a: float) -> float:
        """calculate the eccentricity of an orbit

        :param p: semi-latus rectum in km
        :type p: float
        :param a: semi-major axis in km
        :type a: float
        :return: eccentricity
        :rtype: float
        """
        return sqrt(1 - p / a)

    @staticmethod
    def raan_from_w(w: Vector3D) -> float:
        """calculate the right ascension of the ascending node

        :param w: normalized momentum vector
        :type w: Vector3D
        :return: right ascension of the ascending node in radians
        :rtype: float
        """
        raan: float = atan2(w.x, -w.y)
        if raan < 0:
            raan += 2 * pi
        return raan

    @staticmethod
    def eccentric_anomaly_from_rdv_r_a_n(r_dot_v: float, r: float, a: float, n: float) -> float:
        """calculate eccentric anomaly

        :param r_dot_v: dot product of position and velocity
        :type r_dot_v: float
        :param r: magnitude of position in km
        :type r: float
        :param a: semi-major axis in km
        :type a: float
        :param n: mean motion in radians per second
        :type n: float
        :return: eccentric anomaly in radians
        :rtype: float
        """
        ea: float = atan2(r_dot_v / (a * a * n), 1 - r / a)
        if ea < 0:
            ea += 2 * pi
        return ea

    @staticmethod
    def mean_anomaly_from_ea_and_e(ea: float, e: float) -> float:
        """calculate mean anomaly

        :param ea: eccentric anomaly in radians
        :type ea: float
        :param e: eccentricity
        :type e: float
        :return: mean anomaly in radians
        :rtype: float
        """
        ma: float = ea - e * sin(ea)
        if ma < 0:
            ma += 2 * pi
        elif ma > 2 * pi:
            ma -= 2 * pi
        return ma

    @staticmethod
    def argument_of_latitude_from_r_and_w(r: Vector3D, w: Vector3D) -> float:
        """calculate the argument of latitude

        :param r: position vector
        :type r: Vector3D
        :param w: normalized areal velocity vector
        :type w: Vector3D
        :return: argument of latitude in radians
        :rtype: float
        """
        u: float = atan2(r.z, -r.x * w.y + r.y * w.x)
        if u < 0:
            u += 2 * pi
        return u

    @staticmethod
    def true_anomaly_from_e_and_ea(e: float, ea: float) -> float:
        """calculate true anomaly

        :param e: eccentricity
        :type e: float
        :param ea: eccentric anomaly in radians
        :type ea: float
        :return: true anomaly in radians
        :rtype: float
        """
        ta: float = atan2(sqrt(1 - e * e) * sin(ea), cos(ea) - e)
        if ta < 0:
            ta += 2 * pi
        return ta

    @staticmethod
    def argument_of_perigee_from_u_and_ta(u: float, ta: float) -> float:
        """calculate the argument of perigee

        :param u: argument of latitude in radians
        :type u: float
        :param ta: true anomaly in radians
        :type ta: float
        :return: argument of perigee in radians
        :rtype: float
        """
        aop: float = u - ta
        if aop < 0:
            aop += 2 * pi
        return aop

    def eccentric_anomaly(self) -> float:
        """calculate the eccentric anomaly

        :return: eccentric anomaly in radians
        :rtype: float
        """
        return ClassicalElements.mean_anomaly_to_eccentric_anomaly(self.mean_anomaly, self.eccentricity)

    def perigee_vector(self) -> Vector3D:
        """calculate the vector pointing from the focus to the lowest point in the orbit

        :return: vector from origin to perigee
        :rtype: Vector3D
        """
        cw: float = cos(self.argument_of_perigee)
        c0: float = cos(self.raan)
        sw: float = sin(self.argument_of_perigee)
        s0: float = sin(self.raan)
        ci: float = cos(self.inclination)
        return Vector3D(cw * c0 - sw * ci * s0, cw * s0 + sw * ci * c0, sw * sin(self.inclination)).normalized()

    def semilatus_rectum_vector(self) -> Vector3D:
        """calculate the vector from the focus to the point 90 degrees off of the perigee vector

        :param epoch: _description_
        :type epoch: Epoch
        :return: semi-latus rectum vector
        :rtype: Vector3D
        """
        cw: float = cos(self.argument_of_perigee)
        c0: float = cos(self.raan)
        sw: float = sin(self.argument_of_perigee)
        s0: float = sin(self.raan)
        ci: float = cos(self.inclination)
        return Vector3D(-sw * c0 - cw * ci * s0, -sw * s0 + cw * ci * c0, cw * sin(self.inclination))

    def to_gcrf_state(self) -> GCRFstate:
        """calculates the cartesian representation of the element set

        :return: inertial state of the element set
        :rtype: GCRFstate
        """
        p: Vector3D = self.perigee_vector()
        q: Vector3D = self.semilatus_rectum_vector()

        ea: float = self.eccentric_anomaly()
        cea: float = cos(ea)
        sea: float = sin(ea)

        r: float = self.semimajor_axis * (1 - self.eccentricity * cea)

        ea_dot: float = (1 / r) * sqrt(Earth.MU / self.semimajor_axis)

        b: float = self.semimajor_axis * sqrt(1 - self.eccentricity * self.eccentricity)
        x_bar: float = self.semimajor_axis * (cea - self.eccentricity)
        y_bar: float = b * sea
        x_bar_dot: float = -self.semimajor_axis * ea_dot * sea
        y_bar_dot: float = b * ea_dot * cea

        pos: Vector3D = p.scaled(x_bar).plus(q.scaled(y_bar))
        vel: Vector3D = p.scaled(x_bar_dot).plus(q.scaled(y_bar_dot))

        gmst: float = self.epoch.greenwich_hour_angle()
        itrf_pos: Vector3D = pos.rotation_about_axis(Vector3D(0, 0, 1), -gmst)
        itrf_vel: Vector3D = vel.rotation_about_axis(Vector3D(0, 0, 1), -gmst)
        return ITRFstate(self.epoch, itrf_pos, itrf_vel).gcrf_state()
