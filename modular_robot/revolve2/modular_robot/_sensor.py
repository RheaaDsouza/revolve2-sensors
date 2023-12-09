from revolve2.simulation.actor import Color

from ._module import Module
from ._right_angles import RightAngles

# Define the sensor classes and their corresponding names
sensor_classes = {
    'accelerometer': 'accelerometer',
    'magnetometer': 'magnetometer',
    'gyro': 'gyro',
    'touch': 'touch',
    'rangefinder': 'rangefinder',
}

class Sensor(Module):


    FRONT = 0
    RIGHT = 1
    LEFT = 2

    def __init__(self, sensor_name, rotation: float | RightAngles, color: Color = Color(255, 0, 0, 255)):
        """
        Initialize a sensor.

        :param sensor_name: Name of the sensor type (e.g., 'accelerometer', 'magnetometer', etc.).
        :param rotation: Orientation of the sensor relative to its parent.
        :param color: The color of the sensor module.
        """
        if isinstance(rotation, RightAngles):
            rotation_converted = rotation.value
        else:
            rotation_converted = rotation
        super().__init__(3, rotation_converted, color)
        self.sensor_name = sensor_name
    

    def _add_sensor(self):
        # Create the sensor tag with the dynamically determined name
        sensor_tag = xml.Element(self.sensor_name)
        return sensor_tag

    @property
    def front(self) -> Module | None:
        """
        Get the module attached to the front of the brick.

        :returns: The attached module.
        """
        return self.children[self.FRONT]

    @front.setter
    def front(self, module: Module) -> None:
        """
        Set the module attached to the front of the brick.

        :param module: The module to attach.
        """
        self.children[self.FRONT] = module

    @property
    def right(self) -> Module | None:
        """
        Get the module attached to the right of the brick.

        :returns: The attached module.
        """
        return self.children[self.RIGHT]

    @right.setter
    def right(self, module: Module) -> None:
        """
        Set the module attached to the right of the brick.

        :param module: The module to attach.
        """
        self.children[self.RIGHT] = module

    @property
    def left(self) -> Module | None:
        """
        Get the module attached to the left of the brick.

        :returns: The attached module.
        """
        return self.children[self.LEFT]

    @left.setter
    def left(self, module: Module) -> None:
        """
        Set the module attached to the left of the brick.

        :param module: The module to attach.
        """
        self.children[self.LEFT] = module

