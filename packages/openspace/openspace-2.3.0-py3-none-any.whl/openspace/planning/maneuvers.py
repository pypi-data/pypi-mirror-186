from math import sqrt

from openspace.bodies.celestial import Earth


class VisViva:
    """class used to perform calculations related to the vis-viva law

    :return: velocities for various orbit conditions
    :rtype: float
    """

    @staticmethod
    def circular_velocity(r: float) -> float:
        """calculate the velocity of a circular orbit

        :param r: sma of the circular orbit in km
        :type r: float
        :return: velocity in km/s
        :rtype: float
        """
        return sqrt(Earth.MU / r)

    @staticmethod
    def eccentric_velocity(r: float, a: float) -> float:
        """calculate the velocity at a position in an eccentric orbit

        :param r: current radius in km
        :type r: float
        :param a: semi-major axis in km
        :type a: float
        :return: velocity at the given radius in km/s
        :rtype: float
        """
        return sqrt(Earth.MU * (2 / r - 1 / a))


class Hohmann:
    def __init__(self, r1: float, r2: float) -> None:
        """calculate details of a hohmann transfer going from one circular orbit to another

        :param r1: sma of initial circular orbit
        :type r1: float
        :param r2: sma of final circular orbit
        :type r2: float
        """
        sma: float = (r1 + r2) / 2
        #: velocity prior to the first burn in km/s
        self.initial_velocity: float = VisViva.circular_velocity(r1)

        #: velocity after the first burn in km/s
        self.transfer_velocity_1: float = VisViva.eccentric_velocity(r1, sma)

        #: velocity prior to the second burn in km/s
        self.transfer_velocity_2: float = VisViva.eccentric_velocity(r2, sma)

        #: velocity after the second burn in km/s
        self.final_velocity: float = VisViva.circular_velocity(r2)

        #: magnitude of the first burn in km/s
        self.delta_v_1: float = self.transfer_velocity_1 - self.initial_velocity

        #: magnitude of the second burn in km/s
        self.delta_v_2: float = self.final_velocity - self.transfer_velocity_2
