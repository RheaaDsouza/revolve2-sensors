"""
Simulate and visualize a single modular robot.

You learn:
- How to create a robot body with a basic controller.
- How to simulate and see a robot.
"""

import asyncio

from revolve2.ci_group import terrains, modular_robots
from revolve2.ci_group.logging import setup_logging
from revolve2.ci_group.rng import make_rng
from revolve2.ci_group.simulation import create_batch_single_robot_standard
from revolve2.modular_robot import ActiveHinge, Body, Brick, ModularRobot, RightAngles
from revolve2.modular_robot.brains import BrainCpgNetworkNeighborRandom
from revolve2.simulators.mujoco import LocalRunner


def main() -> None:
    """Run the simulation."""
    # Set up a random number generater, used later.
    RNG_SEED = 5
    rng = make_rng(RNG_SEED)

    # Create a body for the robot.
    body = modular_robots.gecko()
    # Create a brain for the robot.
    # We choose a 'CPG' brain with random parameters (the exact working will not be explained here).
    brain = BrainCpgNetworkNeighborRandom(rng)
    # Combine the body and brain into a modular robot.
    robot = ModularRobot(body, brain)

    # Create a batch containing the robot in a flat terrain.
    # A batch describes a set of simulations to perform.
    # In this case there is a single simulation containing a single robot.
    # We use the 'standard' parameters for robot simulation.
    # You probably don't have to worry about this, but if you are interested, take a look inside the function.
    batch = create_batch_single_robot_standard(
        robot=robot,
        terrain=terrains.flat_with_box(
            size=(10, 10),
            ruggedness=0.2,
            curviness=0.0,
            granularity_multiplier=1.0,
            box_height=2.5
        ),
        addSensor=True,
        sensorConfig = [
            { 
                "type": "gyro", 
                "name": "gyro",
            },
        ],
    )

    # Create a runner that will perform the simulation.
    # This tutorial chooses to use Mujoco, but your version of revolve might contain other simulators as well.
    runner = LocalRunner()
    # Here we use the runner to run a batch.
    # Once a runner finishes a batch, it can be reused to run a new batch.
    # (We only run one batch in this tutorial, so we only use the runner once.)
    asyncio.run(runner.run_batch(batch))


if __name__ == "__main__":
    main()
