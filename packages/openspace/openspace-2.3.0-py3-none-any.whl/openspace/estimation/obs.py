from math import cos, sin

from openspace.coordinates import GCRFstate, ITRFstate, LLAstate, SphericalPosition
from openspace.math.linalg import Matrix3D, Vector3D
from openspace.time import Epoch


class Observation:
    """super class used for space-based and ground-based observations"""

    def __init__(self) -> None:
        pass

    def eci_position(self) -> Vector3D:
        pass

    def epoch(self) -> Epoch:
        pass


class SpaceObservation(Observation):
    def __init__(
        self, observer_state: GCRFstate, observed_direction: Vector3D, r_error: float, ang_error: float
    ) -> None:
        """object used for state estimation when the observer is a space asset

        :param observer_state: inertial state of the observer at the time of the observation
        :type observer_state: GCRFstate
        :param observed_direction: GCRF direction of the object from the observer
        :type observed_direction: Vector3D
        :param r_error: one-sigma error of the observed range in km
        :type r_error: float
        :param ang_error: one-sigma error of the angles in radians
        :type ang_error: float
        """
        #: inertial state of the observer at the time of the observation
        self.observer_state: GCRFstate = observer_state.copy()

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

    def eci_position(self) -> Vector3D:
        """calculate the inertial position of the observation

        :return: inertial position of the observation in the CIS frame
        :rtype: Vector3D
        """
        gmst: float = self.observer_state.epoch.greenwich_hour_angle()
        itrf_ob: Vector3D = GCRFstate(
            self.epoch(), self.observer_state.position.plus(self.observed_direction), Vector3D(0, 0, 0)
        ).itrf_position()
        return itrf_ob.rotation_about_axis(Vector3D(0, 0, 1), gmst)


class GroundObservation(Observation):
    def __init__(
        self, observer_state: ITRFstate, observed_direction: Vector3D, r_error: float, ang_error: float
    ) -> None:
        """used to perform operations related to ground site measurements

        :param observer_state: geocentric coordinates of the observer
        :type observer_state: ITRFstate
        :param observed_direction: ENZ direction of object from observer
        :type observed_direction: Vector3D
        :param r_error: one-sigma error of the observed range in km
        :type r_error: float
        :param ang_error: one-sigma error of the angles in radians
        :type ang_error: float
        """
        #: geocentric state of the observer at the time of the observation
        self.observer_state: ITRFstate = observer_state.copy()

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
        cls, observer_state: ITRFstate, az: float, el: float, r: float, r_error: float, ang_error: float
    ) -> "GroundObservation":
        """create an observation from azimuth, elevation, and range

        :param observer_state: geocentric coordinates of the observer
        :type observer_state: ITRFstate
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

    def eci_position(self) -> Vector3D:
        """calculate the inertial position of the observation

        :return: inertial position of the observation in the CIS frame
        :rtype: Vector3D
        """
        lla_site: LLAstate = self.observer_state.lla_state()
        slamb: float = sin(lla_site.longitude)
        clamb: float = cos(lla_site.longitude)
        spsi: float = sin(lla_site.latitude)
        cpsi: float = cos(lla_site.latitude)

        enz_matrix: Matrix3D = Matrix3D(
            Vector3D(-slamb, clamb, 0.0),
            Vector3D(-spsi * clamb, -spsi * slamb, cpsi),
            Vector3D(cpsi * clamb, cpsi * slamb, spsi),
        )

        gmst: float = self.observer_state.epoch.greenwich_hour_angle()
        itrf_ob: Vector3D = (
            enz_matrix.transpose().multiply_vector(self.observed_direction).plus(self.observer_state.position)
        )
        return itrf_ob.rotation_about_axis(Vector3D(0, 0, 1), gmst)

    def gcrf_position(self) -> Vector3D:
        """calculate the inertial position of the observation

        :return: inertial position of the observation in the GCRF frame
        :rtype: Vector3D
        """

        lla_site: LLAstate = self.observer_state.lla_state()
        slamb: float = sin(lla_site.longitude)
        clamb: float = cos(lla_site.longitude)
        spsi: float = sin(lla_site.latitude)
        cpsi: float = cos(lla_site.latitude)

        enz_matrix: Matrix3D = Matrix3D(
            Vector3D(-slamb, clamb, 0.0),
            Vector3D(-spsi * clamb, -spsi * slamb, cpsi),
            Vector3D(cpsi * clamb, cpsi * slamb, spsi),
        )

        itrf_ob: Vector3D = (
            enz_matrix.transpose().multiply_vector(self.observed_direction).plus(self.observer_state.position)
        )
        return ITRFstate(self.observer_state.epoch, itrf_ob, Vector3D(0, 0, 0)).gcrf_position()
