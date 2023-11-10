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
    def __init__(self, sensor_name, rotation: float | RightAngles, color: Color = Color(255, 0, 0, 255)):
        """
        Initialize a sensor.

        :param sensor_name: Name of the sensor type (e.g., 'accelerometer', 'magnetometer', etc.).
        :param rotation: Orientation of the sensor relative to its parent.
        :param color: The color of the sensor module.
        """
        super().__init__(1, rotation, color)
        self.sensor_name = sensor_name
    

    def _add_sensors(self):
        # Create the sensor tag with the dynamically determined name
        sensor_tag = xml.Element(self.sensor_name)
        return sensor_tag
