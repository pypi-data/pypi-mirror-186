from math import atan2, cos, pi, radians, sin, sqrt
from typing import List

from openspace.math.constants import HOURS_IN_DAY, MINUTES_IN_DAY, MINUTES_IN_HOUR, SECONDS_IN_DAY, SECONDS_IN_HOUR
from openspace.math.linalg import Vector3D


class Conversions:
    """class used to perform various unit conversions

    :return: defined by each static method
    :rtype: defined by each static method
    """

    @staticmethod
    def hms_to_decimal_day(hr: float, m: float, s: float) -> float:
        """calculate the float value of the day given an hour, minute, second representation

        :param hr: hour of day
        :type hr: float
        :param m: minute of day
        :type m: float
        :param s: second of day
        :type s: float
        :return: the time in days
        :rtype: float
        """
        return hr / HOURS_IN_DAY + m / MINUTES_IN_DAY + s / SECONDS_IN_DAY

    @staticmethod
    def dms_to_radians(d: float, m: float, s: float) -> float:
        """calculate an angle in radians that has been defined in degrees, minutes, and seconds

        :param d: degrees in angle
        :type d: float
        :param m: minute of angle
        :type m: float
        :param s: second of angle
        :type s: float
        :return: angle in radians
        :rtype: float
        """
        return radians(d + m / MINUTES_IN_HOUR + s / SECONDS_IN_HOUR)


def sign(num: float) -> float:
    """function to determine if a value is positive or negative

    :param num: expression to be signed
    :type num: float
    :return: 1 if positive -1 if negative 0 if neither
    :rtype: float
    """
    val = 0
    if num > 0:
        val = 1
    elif num < 0:
        val = -1
    return val


class LegendrePolynomial:
    def __init__(self, phi: float) -> None:
        """stores the explicit solution to normalized legendre polynomials used in the geopotential calculations

        :param phi: geodetic latitude in radians
        :type phi: float
        """
        cos_phi: float = cos(phi)
        sin_phi: float = sin(phi)
        cos_phi_squared: float = cos_phi * cos_phi
        sin_phi_squared: float = sin_phi * sin_phi

        #: the polynomial list of lists with indices n, m
        self.p: List[List[float]] = [
            [1, 0],
            [sin_phi, cos_phi, 0],
            [
                (3 * sin_phi_squared - 1) * 0.5,
                3 * sin_phi * cos_phi,
                3 * cos_phi_squared,
                0,
            ],
            [
                sin_phi * (5 * sin_phi_squared - 3) * 0.5,
                (15 * sin_phi_squared - 3) * cos_phi * 0.5,
                15 * sin_phi * cos_phi_squared,
                15 * cos_phi_squared * cos_phi,
                0,
            ],
            [
                0.125 * (35 * sin_phi_squared * sin_phi_squared - 30 * sin_phi_squared + 3),
                2.5 * (7 * sin_phi_squared * sin_phi - 3 * sin_phi) * cos_phi,
                (7 * sin_phi_squared - 1) * cos_phi_squared * 7.5,
                105 * cos_phi * cos_phi_squared * sin_phi,
                105 * cos_phi_squared * cos_phi_squared,
                0,
            ],
        ]


class Eccentricity:
    """Class used to solve eccentricity of an ellipse (e)"""

    @staticmethod
    def from_a_c(a: float, c: float) -> float:
        """calculate eccentricity using equation 1-2 in Vallado 4th Edition

        :param a: semi-major axis in km
        :type a: float
        :param c: half the distance between focii in km
        :type c: float
        :return: eccentricity
        :rtype: float
        """
        return c / a

    @staticmethod
    def from_a_b(a: float, b: float) -> float:
        """calculate eccentricity using equation 1-6 in Vallado 4th Edition

        :param a: semi-major axis in km
        :type a: float
        :param b: semi-minor axis in km
        :type b: float
        :return: eccentricity
        :rtype: float
        """
        return sqrt(a * a - b * b) / a

    @staticmethod
    def from_a_p(a: float, p: float) -> float:
        """calculate eccentricity using equation 2.62 in Satellite Orbits

        :param a: semi-major axis in km
        :type a: float
        :param p: semi-parameter
        :type p: float
        :return: eccentricity
        :rtype: float
        """
        return sqrt(1 - p / a)


class Flattening:
    """class used to solve flattening of an ellipse (f)"""

    @staticmethod
    def from_a_b(a: float, b: float) -> float:
        """calculate flattening using equation 1-3 in Vallado 4th Edition

        :param a: semi-major axis in km
        :type a: float
        :param b: semi-minor axis in km
        :type b: float
        :return: flattening
        :rtype: float
        """
        return (a - b) / a


class SemiMajorAxis:
    """class used to solve semi-major axis of an ellipse (a)"""

    @staticmethod
    def from_mu_n(mu: float, n: float) -> float:
        """calculate semi-major axis using equation 1-29 in Vallado 4th Edition

        :param mu: gravitational constant time mass of central body
        :type mu: float
        :param n: mean motion in radians/s
        :type n: float
        :return: semi-major axis in km
        :rtype: float
        """
        return (mu / (n * n)) ** (1 / 3)

    @staticmethod
    def from_mu_tau(mu: float, tau: float) -> float:
        """calculate semi-major axis using equation 1-27 in Vallado 4th Edition

        :param mu: gravitational constant times mass of central body
        :type mu: float
        :param tau: period in seconds
        :type tau: float
        :return: semi-major axis in km
        :rtype: float
        """
        base: float = tau / (2 * pi)
        return (mu * base * base) ** (1 / 3)

    @staticmethod
    def from_mu_r_v(mu: float, r: float, v: float) -> float:
        """calculate the semi-major axis in km using equation 1-31 in Vallado 4th Edition

        :param mu: gravitational constant times mass of central body
        :type mu: float
        :param r: magnitude of the position vector in km
        :type r: float
        :param v: magnitude of the velocity vector in km/s
        :type v: float
        :return: semi-major axis in km
        :rtype: float
        """
        return 1 / (2 / r - v * v / mu)


class SemiMinorAxis:
    """class used to solve semi-minor axis of an ellipse (b)" """

    @staticmethod
    def from_a_e(a: float, e: float) -> float:
        """calculate semi-minor axis using equation 1-4 in Vallado 4th Edition

        :param a: semi-major axis in km
        :type a: float
        :param e: eccentricity
        :type e: float
        :return: semi-minor axis
        :rtype: float
        """
        return a * sqrt(1 - e * e)


class SemiParameter:
    """class used to solve the semi-parameter of an ellipse (p)"""

    @staticmethod
    def from_a_b(a: float, b: float) -> float:
        """calculate the semi-parameter using equation 1-9 in Vallado 4th Edition

        :param a: semi-major axis in km
        :type a: float
        :param b: semi-minor axis in km
        :type b: float
        :return: semi-parameter in km
        :rtype: float
        """
        return b * b / a

    @staticmethod
    def from_a_e(a: float, e: float) -> float:
        """calculate the semi-parameter using equation 1-10 in Vallado 4th Edition

        :param a: semi-major axis in km
        :type a: float
        :param e: eccentricity
        :type e: float
        :return: semi-parameter in km
        :rtype: float
        """
        return a * (1 - e * e)

    @staticmethod
    def from_mu_h(mu: float, h: float) -> float:
        """calculate the semi-parameter using equation 1-19 in Vallado 4th Edition

        :param mu: gravitational constant time mass of central body
        :type mu: float
        :param h: areal velocity in km^2/s
        :type h: float
        :return: semi-parameter in km
        :rtype: float
        """
        return h * h / mu


class ArealVelocity:
    """class used to calculate areal velocities of an orbit (h)"""

    @staticmethod
    def from_r_v_phi(r: float, v: float, phi: float) -> float:
        """calculate the areal velocity using equation 1-16 in Vallado 4th Edition

        :param r: magnitude of the position vector in km
        :type r: float
        :param v: magnitude of the velocity vector in km/s
        :type v: float
        :param phi: flight path angle (90 - angle between r and v)
        :type phi: float
        :return: areal velocity in km^2/s
        :rtype: float
        """
        return r * v * cos(phi)

    @staticmethod
    def from_mu_p(mu: float, p: float) -> float:
        """calculate the areal velocity using equation 1-19 in Vallado 4th Edition

        :param mu: gravitational constant times mass of central body
        :type mu: float
        :param p: semi-parameter in km
        :type p: float
        :return: areal velocity in km^2/s
        :rtype: float
        """
        return sqrt(mu * p)

    @staticmethod
    def from_r_v(r: Vector3D, v: Vector3D) -> Vector3D:
        """calculate the momentum vector

        :param r: position vector in km
        :type r: Vector3D
        :param v: velocity vector in km/s
        :type v: Vector3D
        :return: areal velocity vector in km^2/s
        :rtype: Vector3D
        """
        return r.cross(v)


class RAAN:
    """static class used to solve right ascension of ascending node"""

    @staticmethod
    def from_w(w: Vector3D) -> float:
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


class Inclination:
    """static class used to solve inclination"""

    @staticmethod
    def from_w(w: Vector3D) -> float:
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


class Radius:
    """static class used to solve the radius of an orbit"""

    @staticmethod
    def from_p_e_nu(p: float, e: float, nu: float) -> float:
        """calculate the radius of an orbit using equation 1-24 in Vallado 4th Edition

        :param p: semi-parameter in km
        :type p: float
        :param e: eccentricity
        :type e: float
        :param nu: true anomaly in radians
        :type nu: float
        :return: radius in km
        :rtype: float
        """
        return p / (1 + e * cos(nu))


class SpecificMechanicalEnergy:
    """static class used to solve specific mechanical energy (Xi)"""

    @staticmethod
    def from_mu_r_v(mu: float, r: float, v: float) -> float:
        """calculate the specific mechanical energy using equation 1-20 in Vallado 4th Edition

        :param mu: gravitational constant times mass of central body
        :type mu: float
        :param r: distance from center of central body in km
        :type r: float
        :param v: magnitude of velocity vector in km/s
        :type v: float
        :return: specific mechanical energy
        :rtype: float
        """
        return v * v * 0.5 - mu / r

    @staticmethod
    def from_mu_a(mu: float, a: float) -> float:
        """calculate specific mechanical energy using equation 1-21 in Vallado 4th Edition

        :param mu: gravitational constant times mass of central body
        :type mu: float
        :param a: semi-major axis in km
        :type a: float
        :return: specific mechanical energy
        :rtype: float
        """
        return -0.5 * mu / a


class VisVivaVelocity:
    """class used to calculate the velocity of an orbit (v)"""

    @staticmethod
    def from_a_mu_r(a: float, mu: float, r: float) -> float:
        """calculate magnitude of velocity using equation 1-22 in Vallado 4th Edition

        :param a: semi-major axis in km
        :type a: float
        :param mu: gravitational constant times mass
        :type mu: float
        :param r: distance from center of central body in km
        :type r: float
        :return: velocity magnitude in km/s
        :rtype: float
        """
        return sqrt(mu * (2 / r - 1 / a))

    @staticmethod
    def from_mu_r_xi(mu: float, r: float, xi: float) -> float:
        """calculate the magnitude of velocity using equation 1-30 in Vallado 4th Edition

        :param mu: gravitational constant times mass
        :type mu: float
        :param r: distance from center of central body in km
        :type r: float
        :param xi: specific mechanical energy
        :type xi: float
        :return: velocity in km/s
        :rtype: float
        """
        return sqrt(2 * (mu / r + xi))

    @staticmethod
    def from_mu_r_e_nu(mu: float, r: float, e: float, nu: float) -> float:
        """calculate the magnitude of velocity using equation 1-32 in Vallado 4th Edition

        :param mu: gravitational constant times mass
        :type mu: float
        :param r: distance from center of central body in km
        :type r: float
        :param e: eccentricity
        :type e: float
        :param nu: true anomaly in radians
        :type nu: float
        :return: velocity in km/s
        :rtype: float
        """
        return sqrt((mu / r) * (2 - (1 - e * e) / (1 + e * cos(nu))))


class Period:
    """class used to calculate the period of an orbit (tau)"""

    @staticmethod
    def from_a_mu(a: float, mu: float) -> float:
        """calculate the period using equation 1-26 in Vallado 4th Edition

        :param a: semi-major axis in km
        :type a: float
        :param mu: gravitational constant times mass of central body
        :type mu: float
        :return: period in seconds
        :rtype: float
        """
        return 2 * pi * sqrt(a * a * a / mu)


class MeanMotion:
    """class used to calculate mean motion of an orbit (n)"""

    @staticmethod
    def from_a_mu(a: float, mu: float) -> float:
        """calculate the mean motion using equation 1-27 in Vallado 4th Edition

        :param a: semi-major axis
        :type a: float
        :param mu: gravitational constant times mass of central body
        :type mu: float
        :return: mean motion in radians/s
        :rtype: float
        """
        return sqrt(mu / (a * a * a))

    @staticmethod
    def from_tau(tau: float) -> float:
        """calculate mean motion using equation 1-27 in Vallado 4th Edition

        :param tau: period of orbit in seconds
        :type tau: float
        :return: mean motion in radians/s
        :rtype: float
        """
        return 2 * pi / tau


class EccentricAnomaly:
    """class used to solve eccentric anomaly"""

    TOLERANCE: float = 1e-12

    @staticmethod
    def from_ma_e(ma: float, e: float) -> float:
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
            if abs(ean - ea0) < EccentricAnomaly.TOLERANCE:
                converged = True
            else:
                ea0 = ean

        if ean < 0:
            ean += 2 * pi

        return ean

    @staticmethod
    def from_rdv_r_a_n(r_dot_v: float, r: float, a: float, n: float) -> float:
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


class TrueAnomaly:
    """static class used to solve true anomaly"""

    @staticmethod
    def from_e_ea(e: float, ea: float) -> float:
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


class ArgumentOfPerigee:
    """static class used to solve argument of perigee"""

    @staticmethod
    def from_u_nu(u: float, nu: float) -> float:
        """calculate the argument of perigee

        :param u: argument of latitude in radians
        :type u: float
        :param nu: true anomaly in radians
        :type nu: float
        :return: argument of perigee in radians
        :rtype: float
        """
        aop: float = u - nu
        if aop < 0:
            aop += 2 * pi
        return aop


class ArgumentOfLatitude:
    """static class used to solve argument of latitude"""

    @staticmethod
    def from_r_w(r: Vector3D, w: Vector3D) -> float:
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


class MeanAnomaly:
    """static class used to solve mean anomaly"""

    @staticmethod
    def from_ea_e(ea: float, e: float) -> float:
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


class EquationsOfMotion:
    """class used to solve equations of motion"""

    #: used to solve semi-major axis
    A = SemiMajorAxis

    #: used to solve semi-minor axis
    B = SemiMinorAxis

    #: used to solve semi-parameter
    P = SemiParameter

    #: used to solve eccentricity
    E = Eccentricity

    #: used to solve period
    TAU = Period

    #: used to solve mean motion
    N = MeanMotion

    #: used to solve velocity
    V = VisVivaVelocity

    #: used to solve specific mechanical energy
    XI = SpecificMechanicalEnergy

    #: used to solve areal velocity
    H = ArealVelocity

    #: used to solve flattening
    F = Flattening

    #: used to solve eccentric anomaly
    EA = EccentricAnomaly

    #: used to solve inclination
    I = Inclination

    #: used to solve raan
    RAAN = RAAN

    #: used to solve true anomaly
    NU = TrueAnomaly

    #: used to solve argument of perige
    W = ArgumentOfPerigee

    #: used to solve argument of latitude
    U = ArgumentOfLatitude

    #: used to solve mean anomaly
    MA = MeanAnomaly
