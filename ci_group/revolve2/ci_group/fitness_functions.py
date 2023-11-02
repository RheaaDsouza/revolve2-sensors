"""Standard fitness functions for modular robots."""

import math

from revolve2.modular_robot import BodyState


def xy_displacement(begin_state: BodyState, end_state: BodyState) -> float:
    """
    Calculate the distance traveled on the xy-plane by a single modular robot.

    :param begin_state: Begin state of the robot.
    :param end_state: End state of the robot.
    :returns: The calculated fitness.
    """
    return math.sqrt(
        (begin_state.core_position[0] - end_state.core_position[0]) ** 2
        + ((begin_state.core_position[1] - end_state.core_position[1]) ** 2)
    )
def calculate_fitness(begin_state, end_state, sensor_data, sonar_weight=0.5):
    """
    The fitness is calculated as the distance traveled on the xy-plane minus a penalty
    term proportional to the sonar distance, where the penalty is controlled by the sonar_weight.
    If the sonar distance is small (indicating proximity to an object), it will penalize the fitness more.


    :param begin_state: Begin state of the robot.
    :param end_state: End state of the robot.
    :param sensor_data: Dictionary containing sensor data, including sonar distance.
    :param sonar_weight: Weight to apply to the sonar distance in the fitness calculation.
    :returns: The calculated fitness.
    """
    # Calculate the distance traveled on the xy-plane
    distance_traveled = math.sqrt(
        (begin_state.core_position[0] - end_state.core_position[0]) ** 2
        + (begin_state.core_position[1] - end_state.core_position[1]) ** 2
    )

    # Incorporate sonar data into fitness with the specified weight
    sonar_distance = sensor_data.get('sonar_distance', 0.0)
    fitness = distance_traveled - sonar_weight * sonar_distance

    return fitness
