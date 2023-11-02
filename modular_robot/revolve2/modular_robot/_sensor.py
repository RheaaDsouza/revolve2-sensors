from revolve2.simulation.actor import Color

from ._module import Module
from ._right_angles import RightAngles


#TODO: add mujoco sensors
# give a list of sensors to pick from mujoco
# and figure out a dynamic sensor tag to add

sensors = ['accelerometer', 'magnetometer ', 'gyro', 'touch', 'rangefinder']

class Sensor(Module):
    def __init__(self, rotation: float | RightAngles, color: Color = Color(255, 0, 0, 255)):
        """
        Initialize a sensor.

        :param rotation: Orientation of the sensor relative to its parent.
        :param color: The color of the sensor module.
        """
        if isinstance(rotation, RightAngles):
            rotation_converted = rotation.value
        else:
            rotation_converted = rotation
        super().__init__(1, rotation_converted, color)
        self.touched_ground = 0  # Initialize the touch ground state to 0 (not touching)
        self.sonar_distance = 0.0  # Initialize sonar distance to 0.0

    def _add_sensors(self):
        return 0

    def toggle_touch_ground(self):
        """
        Toggle the touch ground state of the sensor.

        When called, this method will toggle the `touched_ground` state between 0 and 1.
        """
        self.touched_ground = 1 if self.touched_ground == 0 else 0

    def is_touching_ground(self) -> bool:
        """
        Check if the sensor is currently touching the ground.

        :returns: True if the sensor is touching the ground (touched_ground = 1), False otherwise.
        """
        return self.touched_ground == 1

    def set_sonar_distance(self, distance: float):
        """
        Set the sonar distance detected by the sensor.

        :param distance: The distance detected by the sonar sensor.
        """
        self.sonar_distance = distance

    def get_sonar_distance(self) -> float:
        """
        Get the sonar distance detected by the sensor.

        :returns: The distance detected by the sonar sensor.
        """
        return self.sonar_distance
