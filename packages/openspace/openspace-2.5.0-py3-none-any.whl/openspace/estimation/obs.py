from openspace.coordinates.positions import LLA, PositionConvert, SphericalPosition
from openspace.coordinates.states import GCRF, ITRF
from openspace.math.linalg import Vector3D
from openspace.time import Epoch


class Observation:
    """super class used for space-based and ground-based observations"""

    def __init__(self) -> None:
        pass

    def ijk_position(self) -> Vector3D:
        pass

    def epoch(self) -> Epoch:
        pass

    def observer_ijk(self) -> Vector3D:
        pass


class SpaceObservation(Observation):
    def __init__(self, observer_state: GCRF, observed_direction: Vector3D, r_error: float, ang_error: float) -> None:
        """object used for state estimation when the observer is a space asset

        :param observer_state: inertial state of the observer at the time of the observation
        :type observer_state: GCRF
        :param observed_direction: GCRF direction of the object from the observer
        :type observed_direction: Vector3D
        :param r_error: one-sigma error of the observed range in km
        :type r_error: float
        :param ang_error: one-sigma error of the angles in radians
        :type ang_error: float
        """
        #: inertial state of the observer at the time of the observation
        self.observer_state: GCRF = observer_state.copy()

        #: vector from observer to target in the GCRF frame
        self.observed_direction: Vector3D = observed_direction.copy()

        spherical: SphericalPosition = SphericalPosition.from_cartesian(observed_direction)

        #: magnitude of the observation in km
        self.range: float = spherical.radius

        #: right ascension of the observation in radians
        self.right_ascension: float = spherical.right_ascension

        #: declination of the observation in radians
        self.declination: float = spherical.declination

        #: one-sigma range error of the observation in km
        self.range_error: float = r_error

        #: one-sigma angular error of the observation in radians
        self.angular_error: float = ang_error

    def epoch(self) -> Epoch:
        """get the time the observation was taken

        :return: valid epoch of the observation
        :rtype: Epoch
        """
        return self.observer_state.epoch

    def ijk_position(self) -> Vector3D:
        """calculate the inertial position of the observation

        :return: inertial position of the observation in the IJK frame
        :rtype: Vector3D
        """
        return PositionConvert.gcrf.to_ijk(self.observer_state.position.plus(self.observed_direction), self.epoch())


class GroundObservation(Observation):
    def __init__(self, observer_state: ITRF, observed_direction: Vector3D, r_error: float, ang_error: float) -> None:
        """used to perform operations related to ground site measurements

        :param observer_state: geocentric coordinates of the observer
        :type observer_state: ITRF
        :param observed_direction: ENZ direction of object from observer
        :type observed_direction: Vector3D
        :param r_error: one-sigma error of the observed range in km
        :type r_error: float
        :param ang_error: one-sigma error of the angles in radians
        :type ang_error: float
        """
        #: geocentric state of the observer at the time of the observation
        self.observer_state: ITRF = observer_state.copy()

        #: vector from observer to target in the ENZ frame
        self.observed_direction: Vector3D = observed_direction.copy()

        spherical: SphericalPosition = SphericalPosition.from_cartesian(
            Vector3D(observed_direction.y, observed_direction.x, observed_direction.z)
        )

        #: magnitude of the observation in km
        self.range: float = spherical.radius

        #: azimuth of the observation in radians
        self.azimuth: float = spherical.right_ascension

        #: elevation of the observation in radians
        self.elevation: float = spherical.declination

        #: one-sigma range error of the observation in km
        self.range_error: float = r_error

        #: one-sigma angular error of the observation in radians
        self.angular_error: float = ang_error

    @classmethod
    def from_angles_and_range(
        cls, observer_state: ITRF, az: float, el: float, r: float, r_error: float, ang_error: float
    ) -> "GroundObservation":
        """create an observation from azimuth, elevation, and range

        :param observer_state: geocentric coordinates of the observer
        :type observer_state: ITRF
        :param az: azimuth of the observation in radians
        :type az: float
        :param el: elevation of the observation in radians
        :type el: float
        :param r: magnitude of the observation in km
        :type r: float
        :param r_error: one-sigma range error of the observation in km
        :type r_error: float
        :param ang_error: one-sigma angular error of the observation in radians
        :type ang_error: float
        :return: observation from a terrestrial site
        :rtype: GroundObservation
        """
        nez: Vector3D = SphericalPosition(r, az, el).to_cartesian()
        enz: Vector3D = Vector3D(nez.y, nez.x, nez.z)
        return cls(observer_state, enz, r_error, ang_error)

    def epoch(self) -> Epoch:
        """get the time the observation was taken

        :return: valid epoch of the observation
        :rtype: Epoch
        """
        return self.observer_state.epoch

    def ijk_position(self) -> Vector3D:
        """calculate the inertial position of the observation

        :return: inertial position of the observation in the IJK frame
        :rtype: Vector3D
        """
        lla_site: LLA = PositionConvert.itrf.to_lla(self.observer_state.position)
        itrf_ob: Vector3D = PositionConvert.enz.to_itrf(lla_site, self.observed_direction).plus(
            self.observer_state.position
        )
        return PositionConvert.itrf.to_ijk(itrf_ob, self.epoch())

    def gcrf_position(self) -> Vector3D:
        """calculate the inertial position of the observation

        :return: inertial position of the observation in the GCRF frame
        :rtype: Vector3D
        """
        lla_site: LLA = PositionConvert.itrf.to_lla(self.observer_state.position)
        itrf_ob: Vector3D = PositionConvert.enz.to_itrf(lla_site, self.observed_direction).plus(
            self.observer_state.position
        )
        return PositionConvert.itrf.to_gcrf(itrf_ob, self.epoch())
