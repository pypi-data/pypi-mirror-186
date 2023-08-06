from openspace.coordinates import GCRFstate, SphericalPosition
from openspace.math.linalg import Vector3D


class SpaceObservation:
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
