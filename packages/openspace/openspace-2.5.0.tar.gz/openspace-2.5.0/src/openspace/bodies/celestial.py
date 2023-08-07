from math import cos, radians, sin, sqrt
from typing import List

from openspace.math.constants import SECONDS_IN_SIDEREAL_DAY
from openspace.math.functions import Conversions, EquationsOfMotion
from openspace.math.linalg import Matrix3D, Vector3D
from openspace.time import Epoch


class Earth:

    """Class used to store Earth properties"""

    #: normalized c coefficients used for geopotential calculation
    C: List[List[float]] = [
        [1],
        [0, 0],
        [-0.484165143790815e-3 / sqrt(0.2), -0.206615509074176e-9 / sqrt(0.6), 0.243938357328313e-5 / sqrt(2.4)],
        [
            0.957161207093473e-6 / sqrt(1 / 7),
            0.203046201047864e-5 / sqrt(6 / 7),
            0.904787894809528e-6 / sqrt(60 / 7),
            0.721321757121568e-6 / sqrt(360 / 7),
        ],
        [
            0.539965866638991e-6 / sqrt(24 / 216),
            -0.536157389388867e-6 / sqrt(10 / 9),
            0.350501623962649e-6 / sqrt(20),
            0.990856766672321e-6 / sqrt(280),
            -0.188519633023033e-6 / sqrt(2240),
        ],
    ]

    #: normalized s coefficients used for geopotential calculation
    S: List[List[float]] = [
        [0],
        [0, 0],
        [0, 0.138441389137979e-8 / sqrt(0.6), -0.140027370385934e-5 / sqrt(2.4)],
        [
            0,
            0.248200415856872e-6 / sqrt(6 / 7),
            -0.619005475177618e-6 / sqrt(60 / 7),
            0.141434926192941e-5 / sqrt(360 / 7),
        ],
        [
            0,
            -0.473567346518086e-6 / sqrt(10 / 9),
            0.662480026275829e-6 / sqrt(20),
            -0.200956723567452e-6 / sqrt(280),
            0.308803882149194e-6 / sqrt(2240),
        ],
    ]

    #: the number of zonal and tesseral terms to be used in the gravity calculation
    DEGREE_AND_ORDER: int = len(S)

    #: G*M given in km^3/s^2
    MU: float = 398600.4418

    #: distance from earth center to surface at the equator in km
    RADIUS: float = 6378.137

    #: value defining the ellipsoid of an oblate earth
    FLATTENING: float = 1 / 298.2572235

    #: inclination of ecliptic relative to earth equator in radians
    OBLIQUITY_OF_ECLIPTIC: float = radians(23.43929111)

    #: boolean identifying if gravity will be modeled as a point-source or with non-spherical methods
    USE_GEODETIC_MODEL = True

    @staticmethod
    def obliquity_of_ecliptic_at_epoch(epoch: Epoch) -> float:
        """calculate the obliquity of ecliptic (epsilon) at a given epoch

        :param epoch: time of interest
        :type epoch: Epoch
        :return: true-of-date epsilon
        :rtype: float
        """
        # Equation 5.39
        t = epoch.julian_centuries_past_j2000()

        a = Conversions.dms_to_radians(0, 0, 46.815)
        b = Conversions.dms_to_radians(0, 0, 0.00059)
        c = Conversions.dms_to_radians(0, 0, 0.001813)

        # Equation 5.42
        return Earth.OBLIQUITY_OF_ECLIPTIC - a * t - b * t * t + c * t * t * t

    @staticmethod
    def geo_radius() -> float:
        """calculate the radius of an orbit with a period equal to that of Earth's rotation

        :return: geosynchronous radius in km
        :rtype: float
        """
        return EquationsOfMotion.A.from_mu_tau(Earth.MU, SECONDS_IN_SIDEREAL_DAY)

    @staticmethod
    def rotation(epoch: Epoch) -> Matrix3D:
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

    @staticmethod
    def precession(epoch: Epoch) -> Matrix3D:
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

    @staticmethod
    def nutation(epoch: Epoch) -> Matrix3D:
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


class Sun:

    """class used to store properties of the sun for a force model"""

    #: RAAN + argument of periapsis in radians
    W_PLUS_W = radians(282.94)

    #: cosine of obliquity of ecliptic
    COS_OBLIQUITY = cos(Earth.OBLIQUITY_OF_ECLIPTIC)

    #: sine of obliquity of ecliptic
    SIN_OBLIQUITY = sin(Earth.OBLIQUITY_OF_ECLIPTIC)

    #: G*M in km^3/s^
    MU = 1.327124400419e11

    #: Estimate of srp
    P = 4.56e-6

    #: Distance to earth in km
    AU = 149597870.691

    @staticmethod
    def get_position(epoch: Epoch) -> Vector3D:
        """calculate the ECI position at a given epoch

        :param epoch: time of calculated position vector
        :type epoch: Epoch
        :return: ECI position in km
        :rtype: Vector3D
        """
        a = Conversions.dms_to_radians(0, 0, 6892)
        b = Conversions.dms_to_radians(0, 0, 72)
        t = epoch.julian_centuries_past_j2000()

        ma = radians(357.5256 + 35999.049 * t)

        sma = sin(ma)
        cma = cos(ma)
        c2ma = cos(2 * ma)

        lam = Sun.W_PLUS_W + ma + a * sma + b * 2 * sma * cma
        r = (149.619 - 2.499 * cma - 0.021 * c2ma) * 1e6

        x = r * cos(lam)

        slam = sin(lam)

        y = r * slam * Sun.COS_OBLIQUITY
        z = r * slam * Sun.SIN_OBLIQUITY

        return Vector3D(x, y, z)


class Moon:
    """class used to store properties of the moon to be used in force modeling"""

    #: G*M in km^3/s^2
    MU = 4902.800305555

    #: distance from center of moon to surface in km
    RADIUS = 1737.4000

    @staticmethod
    def get_position(epoch: Epoch) -> Vector3D:
        """calculate ECI position of moon

        :param epoch: time of calculated position vector
        :type epoch: Epoch
        :return: ECI position in km
        :rtype: Vector3D
        """
        # Equation 3.47
        t = epoch.julian_centuries_past_j2000()
        l0 = radians(218.31617 + 481267.88088 * t - 1.3972 * t)
        l = radians(134.96292 + 477198.86753 * t)
        lp = radians(357.52543 + 35999.04944 * t)
        f = radians(93.27283 + 483202.01873 * t)
        d = radians(297.85027 + 445267.11135 * t)

        # Auxiliary variables to store the angles defined in seconds in equation 3.48
        a0 = Conversions.dms_to_radians(0, 0, 22640.0)
        a1 = Conversions.dms_to_radians(0, 0, 769.0)
        a2 = Conversions.dms_to_radians(0, 0, 4586.0)
        a3 = Conversions.dms_to_radians(0, 0, 2370.0)
        a4 = Conversions.dms_to_radians(0, 0, 668.0)
        a5 = Conversions.dms_to_radians(0, 0, 412.0)
        a6 = Conversions.dms_to_radians(0, 0, 212.0)
        a7 = Conversions.dms_to_radians(0, 0, 206.0)
        a8 = Conversions.dms_to_radians(0, 0, 192.0)
        a9 = Conversions.dms_to_radians(0, 0, 165.0)
        a10 = Conversions.dms_to_radians(0, 0, 148.0)
        a11 = Conversions.dms_to_radians(0, 0, 125.0)
        a12 = Conversions.dms_to_radians(0, 0, 110.0)
        a13 = Conversions.dms_to_radians(0, 0, 55.0)

        # Equation 3.48
        lam = (
            l0
            + a0 * sin(l)
            + a1 * sin(2 * l)
            - a2 * sin(l - 2.0 * d)
            + a3 * sin(2.0 * d)
            - a4 * sin(lp)
            - a5 * sin(2.0 * f)
            - a6 * sin(2.0 * l - 2.0 * d)
            - a7 * sin(l + lp - 2.0 * d)
            + a8 * sin(l + 2.0 * d)
            - a9 * sin(lp - 2.0 * d)
            + a10 * sin(l - lp)
            - a11 * sin(d)
            - a12 * sin(l + lp)
            - a13 * sin(2.0 * f - 2.0 * d)
        )

        # Redefined variables for angles in equation 3.49
        a0 = Conversions.dms_to_radians(0, 0, 18520.0)
        a1 = Conversions.dms_to_radians(0, 0, 412.0)
        a2 = Conversions.dms_to_radians(0, 0, 541.0)
        a3 = Conversions.dms_to_radians(0, 0, 526.0)
        a4 = Conversions.dms_to_radians(0, 0, 44.0)
        a5 = Conversions.dms_to_radians(0, 0, 31.0)
        a6 = Conversions.dms_to_radians(0, 0, 25.0)
        a7 = Conversions.dms_to_radians(0, 0, 23.0)
        a8 = Conversions.dms_to_radians(0, 0, 21.0)
        a9 = Conversions.dms_to_radians(0, 0, 11.0)

        # Equation 3.49
        beta = (
            a0 * sin(f + lam - l0 + a1 * sin(2.0 * f + a2 * sin(lp)))
            - a3 * sin(f - 2.0 * d)
            + a4 * sin(l + f - 2.0 * d)
            - a5 * sin(-l + f - 2.0 * d)
            - a6 * sin(-2.0 * l + f)
            - a7 * sin(lp + f - 2.0 * d)
            + a8 * sin(-l + f)
            + a9 * sin(-lp + f - 2.0 * d)
        )

        # Equation 3.50
        r = (
            385000.0
            - 20905.0 * cos(l)
            - 3699.0 * cos(2.0 * d - l)
            - 2956.0 * cos(2.0 * d)
            - 570.0 * cos(2.0 * l)
            + 246.0 * cos(2.0 * l - 2.0 * d)
            - 205.0 * cos(lp - 2.0 * d)
            - 171.0 * cos(l + 2.0 * d)
            - 152.0 * cos(l + lp - 2.0 * d)
        )

        # Equation 3.51
        x = r * cos(lam) * cos(beta)
        y = r * sin(lam) * cos(beta)
        z = r * sin(beta)

        eps = Earth.OBLIQUITY_OF_ECLIPTIC

        return Vector3D(x, y, z).rotation_about_axis(Vector3D(1, 0, 0), eps)
