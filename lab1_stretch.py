import stretch_body.robot

robot = stretch_body.robot.Robot()
robot.startup()

robot.stow()

# Extend arm and lift to full extension
robot.arm.move_to(0.5)
robot.lift.move_to(1.1)
robot.push_command()
robot.arm.wait_until_at_setpoint() # Wait for motion to complete

# Move all three wrist motors one at a time


# Open gripper and close it


# Rotate both of the motors connected to camera


# Move back to stow position


# Drive forward 0.5m, rotate 180deg, drive 0.5m forward


