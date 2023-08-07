from math import asin, atan2, cos, pi, sin, sqrt

from openspace.bodies.celestial import Earth
from openspace.math.functions import sign
from openspace.math.linalg import Matrix3D, Vector3D
from openspace.time import Epoch


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


class ENZ:
    @staticmethod
    def matrix(lamb: float, psi: float) -> Matrix3D:
        """calculate the transformation matrix required for ENZ/ITRF transformations

        :param lamb: geodetic longitude
        :type lamb: float
        :param psi: geodetic latitude
        :type psi: float
        :return: matrix used to go from ITRF to ENZ
        :rtype: Matrix3D
        """
        slamb: float = sin(lamb)
        clamb: float = cos(lamb)
        spsi: float = sin(psi)
        cpsi: float = cos(psi)

        return Matrix3D(
            Vector3D(-slamb, clamb, 0.0),
            Vector3D(-spsi * clamb, -spsi * slamb, cpsi),
            Vector3D(cpsi * clamb, cpsi * slamb, spsi),
        )


class LLA:
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

    def copy(self) -> "LLA":
        """creates a duplicate of the calling state

        :return: state with properties that match that of the calling state
        :rtype: LLA
        """
        return LLA(self.latitude, self.longitude, self.altitude)


class _PositionConvertGCRF:
    """class used to convert GCRF positions to other frames"""

    @staticmethod
    def to_itrf(pos: Vector3D, epoch: Epoch) -> Vector3D:
        """calculate the ITRF position

        :param pos: GCRF position
        :type pos: Vector3D
        :param epoch: epoch for which the position is valid
        :type epoch: Epoch
        :return: ITRF position
        :rtype: Vector3D
        """
        return Earth.rotation(epoch).multiply_vector(_PositionConvertGCRF.to_tod(pos, epoch))

    @staticmethod
    def to_tod(pos: Vector3D, epoch: Epoch) -> Vector3D:
        """calculate the TOD position

        :param pos: GCRF position
        :type pos: Vector3D
        :param epoch: epoch for which the position is valid
        :type epoch: Epoch
        :return: TOD position
        :rtype: Vector3D
        """
        return Earth.nutation(epoch).multiply_vector(_PositionConvertGCRF.to_mod(pos, epoch))

    @staticmethod
    def to_mod(pos: Vector3D, epoch: Epoch) -> Vector3D:
        """calculate the MOD position

        :param pos: GCRF position
        :type pos: Vector3D
        :param epoch: epoch for which the position is valid
        :type epoch: Epoch
        :return: MOD position
        :rtype: Vector3D
        """
        return Earth.precession(epoch).multiply_vector(pos)

    @staticmethod
    def to_ijk(pos: Vector3D, epoch: Epoch) -> Vector3D:
        """calculate the IJK position

        :param pos: GCRF position
        :type pos: Vector3D
        :param epoch: epoch for which the position is valid
        :type epoch: Epoch
        :return: IJK position
        :rtype: Vector3D
        """
        return _PositionConvertITRF.to_ijk(_PositionConvertGCRF.to_itrf(pos, epoch), epoch)


class _PositionConvertITRF:
    """class used to convert ITRF positions to other frames"""

    @staticmethod
    def to_gcrf(pos: Vector3D, epoch: Epoch) -> Vector3D:
        """calculate the GCRF position

        :param pos: ITRF position
        :type pos: Vector3D
        :param epoch: epoch for which the position is valid
        :type epoch: Epoch
        :return: GCRF position
        :rtype: Vector3D
        """
        return Earth.precession(epoch).transpose().multiply_vector(_PositionConvertITRF.to_mod(pos, epoch))

    @staticmethod
    def to_tod(pos: Vector3D, epoch: Epoch) -> Vector3D:
        """calculate the TOD position

        :param pos: ITRF position
        :type pos: Vector3D
        :param epoch: epoch for which the position is valid
        :type epoch: Epoch
        :return: TOD position
        :rtype: Vector3D
        """
        return Earth.rotation(epoch).transpose().multiply_vector(pos)

    @staticmethod
    def to_mod(pos: Vector3D, epoch: Epoch) -> Vector3D:
        """calculate the MOD position

        :param pos: ITRF position
        :type pos: Vector3D
        :param epoch: epoch for which the position is valid
        :type epoch: Epoch
        :return: MOD position
        :rtype: Vector3D
        """
        return Earth.nutation(epoch).transpose().multiply_vector(_PositionConvertITRF.to_tod(pos, epoch))

    @staticmethod
    def to_lla(pos: Vector3D) -> LLA:
        """calculate the LLA position

        :param pos: ITRF position
        :type pos: Vector3D
        :return: LLA position
        :rtype: LLA
        """
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

        return LLA(lamb, phi, h)

    @staticmethod
    def to_ijk(pos: Vector3D, epoch: Epoch) -> Vector3D:
        """calculate the IJK position

        :param pos: ITRF position
        :type pos: Vector3D
        :param epoch: epoch for which the position is valid
        :type epoch: Epoch
        :return: IJK position
        :rtype: Vector3D
        """
        return pos.rotation_about_axis(Vector3D(0, 0, 1), epoch.greenwich_hour_angle())


class _PositionConvertLLA:
    """class used to convert LLA positions to other frames"""

    @staticmethod
    def to_itrf(lla: LLA) -> Vector3D:
        """calculate the ITRF position

        :param lla: LLA position
        :type lla: LLA
        :return: ITRF position
        :rtype: Vector3D
        """
        lat: float = lla.latitude
        longitude: float = lla.longitude
        alt: float = lla.altitude

        f: float = Earth.FLATTENING
        e: float = sqrt(f * (2 - f))
        slat: float = sin(lat)
        clat: float = cos(lat)
        n: float = Earth.RADIUS / sqrt(1 - e * e * slat * slat)

        return Vector3D(
            (n + alt) * clat * cos(longitude), (n + alt) * clat * sin(longitude), (n * (1.0 - e * e) + alt) * slat
        )


class _PositionConvertENZ:
    """class used to convert ENZ positions to other frames"""

    @staticmethod
    def to_itrf(lla: LLA, enz: Vector3D) -> Vector3D:
        """calculate the ITRF position

        :param lla: LLA position of the ENZ origin
        :type lla: LLA
        :param enz: ENZ position from the lla origin
        :type enz: Vector3D
        :return: ITRF position
        :rtype: Vector3D
        """
        return ENZ.matrix(lla.longitude, lla.latitude).transpose().multiply_vector(enz)


class PositionConvert:

    #: used to perform conversions from GCRF
    gcrf = _PositionConvertGCRF

    #: used to perform conversions from ITRF
    itrf = _PositionConvertITRF

    #: used to perform conversions from LLA
    lla = _PositionConvertLLA

    #: used to perform conversions from ENZ
    enz = _PositionConvertENZ
