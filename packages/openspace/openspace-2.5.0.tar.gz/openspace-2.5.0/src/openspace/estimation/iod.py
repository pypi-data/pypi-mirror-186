from math import asin, atan2, cos, pi, sin, sqrt

from openspace.bodies.celestial import Earth
from openspace.coordinates.elements import ClassicalElements
from openspace.estimation.obs import Observation
from openspace.math.constants import SECONDS_IN_DAY
from openspace.math.linalg import Vector3D


class Gauss:

    NU_TOLERANCE: float = 1e-12

    @staticmethod
    def coes_from_positions(ob1: Observation, ob2: Observation) -> ClassicalElements:
        """calculate the orbital elements of a satellite using the gauss method for two position vectors

        :param ob1: first observation
        :type ob1: Observation
        :param ob2: second observation
        :type ob2: Observation
        :return: orbital elements for a spacecraft that travels through the two positions
        :rtype: ClassicalElements
        """

        # method is found in Chapter 2 of Satellite Orbits
        ra: Vector3D = ob1.ijk_position()
        rb: Vector3D = ob2.ijk_position()
        ra_mag: float = ra.magnitude()
        rb_mag: float = rb.magnitude()

        # equation 2.109
        ea: Vector3D = ra.normalized()

        # equation 2.110
        r0: Vector3D = rb.minus(ea.scaled(rb.dot(ea)))
        r0_mag: float = r0.magnitude()
        e0: Vector3D = r0.normalized()

        # equation 2.111
        w: Vector3D = ea.cross(e0)
        ua: float = atan2(ra.z, -ra.x * w.y + ra.y * w.x)
        inc: float = atan2(sqrt(w.x * w.x + w.y * w.y), w.z)
        raan: float = atan2(w.x, -w.y)
        if inc < 0:
            inc += 2 * pi
        if raan < 0:
            raan += 2 * pi

        # equation 2.99
        tau: float = sqrt(Earth.MU) * (ob2.epoch().value - ob1.epoch().value) * SECONDS_IN_DAY

        # equation 2.101
        base: float = 2 * (ra_mag * rb_mag + ra.dot(rb))
        m: float = tau * tau * (base) ** -1.5
        l: float = (ra_mag + rb_mag) / (2 * sqrt(base)) - 0.5

        # equation 2.107
        n0: float = 12 / 22 + 10 / 22 * sqrt(1 + (44 / 9) * (m / (l + 5 / 6)))
        n1: float = n0 + 0.1
        n2: float = n0
        n: float = Gauss.solve_nu(m, l, n1, n2)

        # equation 2.112
        base = ra_mag * r0_mag * n / tau
        p: float = base * base

        # equation 2.114
        ecosva: float = p / ra_mag - 1
        ecosvb: float = p / rb_mag - 1

        # equation 2.116
        esinva: float = (ecosva * (rb.dot(ea) / rb_mag) - ecosvb) / (r0_mag / rb_mag)

        ta: float = atan2(esinva, ecosva)
        if ta < 0:
            ta += 2 * pi

        e: float = ecosva / cos(ta)

        aop: float = ua - ta
        if aop < 0:
            aop += 2 * pi

        sma: float = p / (1 - e * e)

        e_anom: float = atan2(sqrt(1 - e * e) * sin(ta), cos(ta) + e)
        ma: float = e_anom - e * sin(e_anom)

        return ClassicalElements(ob1.epoch(), sma, e, inc, raan, aop, ma)

    @staticmethod
    def solve_nu(m: float, l: float, n0: float, n1: float) -> float:
        """recursively solve for nu in equation 2.105 of Satellite Orbits (secant procedure)

        :param m: auxiliary variable
        :type m: float
        :param l: auxiliary variable
        :type l: float
        :param n0: nu at index i - 1
        :type n0: float
        :param n1: nu at index i
        :type n1: float
        :return: nu at index i + 1
        :rtype: float
        """
        converged: bool = False
        f_of_nu_1: float
        n2: float
        while not converged:
            f_of_nu_1 = Gauss.f_of_nu(n1, m, l)
            n2 = n1 - f_of_nu_1 * (n1 - n0) / (f_of_nu_1 - Gauss.f_of_nu(n0, m, l))
            if abs(n2 - n1) < Gauss.NU_TOLERANCE:
                converged = True
            else:
                n0 = n1
                n1 = n2

        return n2

    @staticmethod
    def f_of_nu(n: float, m: float, l: float) -> float:
        """equation 2.106 in Satellite orbits

        :param n: nu
        :type n: float
        :param m: auxiliary variable
        :type m: float
        :param l: auxiliary variable
        :type l: float
        :return: f(nu)
        :rtype: float
        """
        m_over_nu_squared: float = m / (n * n)
        return 1 - n + m_over_nu_squared * Gauss.w_of_omega(m_over_nu_squared - l)

    @staticmethod
    def w_of_omega(w: float) -> float:
        """equation 2.103 in Satellite Orbits

        :param w: omega
        :type w: float
        :return: w(omega)
        :rtype: float
        """
        g: float = 2 * asin(sqrt(w))
        sg: float = sin(g)
        return (2 * g - sin(2 * g)) / (sg * sg * sg)
