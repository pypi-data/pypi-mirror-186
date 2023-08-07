from openspace.bodies.artificial import Spacecraft
from openspace.coordinates.positions import ENZ, LLA, PositionConvert
from openspace.coordinates.states import ITRF
from openspace.estimation.obs import GroundObservation
from openspace.math.linalg import Matrix3D, Vector3D


class GroundSite:
    def __init__(self, lla: LLA) -> None:
        """used for operations that require modeling of a terrestrial location
        :param lla: state that holds the latitude, longitude, and altitude of the ground station
        :type lla: LLA
        """
        #: geodetic cartesian coordinates of the ground station in km
        self.itrf_position: Vector3D = PositionConvert.lla.to_itrf(lla)

        #: geodetic latitude in radians
        self.latitude: float = lla.latitude

        #: longitude in radians
        self.longitude: float = lla.longitude

        #: matrix used to perform transformations to and from enz/itrf
        self.enz_matrix: Matrix3D = ENZ.matrix(lla.longitude, lla.latitude)

    @classmethod
    def from_itrf_position(cls, itrf: Vector3D) -> "GroundSite":
        """create a groundsite from cartesian coordinates

        :param itrf: earth-fixed position of the groundsite
        :type itrf: Vector3D
        :return: object stationed at the input earth-fixed vector
        :rtype: GroundSite
        """
        return cls(PositionConvert.itrf.to_lla(itrf))

    def enz_position(self, obj_itrf: Vector3D) -> Vector3D:
        """calculates the east-north-zenith coordinates of the argument position

        :param obj_itrf: itrf position of the object of interest
        :type obj_itrf: Vector3D
        :return: transformation of the argument itrf position to the east-north-zenith frame
        :rtype: Vector3D
        """
        return self.enz_matrix.multiply_vector(obj_itrf.minus(self.itrf_position))

    def angles_and_range(self, target: Spacecraft) -> GroundObservation:
        """calculate the topo-centric angles and range to the argument spacecraft

        :param target: spacecraft being observed
        :type target: Spacecraft
        :return: azimuth, elevation, and range to the spacecraft from the ground site
        :rtype: GroundObservation
        """

        return GroundObservation(
            ITRF.from_fixed(target.current_epoch(), self.itrf_position),
            self.enz_position(PositionConvert.gcrf.to_itrf(target.position(), target.current_epoch())),
            0,
            0,
        )
