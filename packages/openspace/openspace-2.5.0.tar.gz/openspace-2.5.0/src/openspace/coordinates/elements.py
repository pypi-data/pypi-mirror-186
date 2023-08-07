from math import cos, sin, sqrt

from openspace.bodies.celestial import Earth
from openspace.coordinates.states import IJK
from openspace.math.functions import EquationsOfMotion
from openspace.math.linalg import Vector3D
from openspace.time import Epoch


class ClassicalElements:
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

    @classmethod
    def from_ijk(cls, state: IJK) -> "ClassicalElements":
        r: float = state.position.magnitude()
        v: float = state.velocity.magnitude()
        rdv: float = state.position.dot(state.velocity)

        h: Vector3D = EquationsOfMotion.H.from_r_v(state.position, state.velocity)
        w: Vector3D = h.normalized()
        i: float = EquationsOfMotion.I.from_w(w)
        raan: float = EquationsOfMotion.RAAN.from_w(w)
        a: float = EquationsOfMotion.A.from_mu_r_v(Earth.MU, r, v)
        p: float = EquationsOfMotion.P.from_mu_h(Earth.MU, h.magnitude())
        e: float = EquationsOfMotion.E.from_a_p(a, p)
        n: float = EquationsOfMotion.N.from_a_mu(a, Earth.MU)
        ea: float = EquationsOfMotion.EA.from_rdv_r_a_n(rdv, r, a, n)
        ma: float = EquationsOfMotion.MA.from_ea_e(ea, e)
        u: float = EquationsOfMotion.U.from_r_w(state.position, w)
        nu: float = EquationsOfMotion.NU.from_e_ea(e, ea)
        aop: float = EquationsOfMotion.W.from_u_nu(u, nu)
        return cls(state.epoch, a, e, i, raan, aop, ma)

    def eccentric_anomaly(self) -> float:
        """calculate the eccentric anomaly

        :return: eccentric anomaly in radians
        :rtype: float
        """
        return EquationsOfMotion.EA.from_ma_e(self.mean_anomaly, self.eccentricity)

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

    def to_ijk(self) -> IJK:
        """calculates the cartesian representation of the element set

        :return: inertial state of the element set
        :rtype: IJK
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

        return IJK(self.epoch, p.scaled(x_bar).plus(q.scaled(y_bar)), p.scaled(x_bar_dot).plus(q.scaled(y_bar_dot)))
