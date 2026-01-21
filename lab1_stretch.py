import time
import stretch_body.robot
robot = stretch_body.robot.Robot()
robot.startup()

robot.stow()
robot.push_command()
robot.wait_command()

# Extend arm and lift to full extension
robot.arm.move_to(0.5)
robot.lift.move_to(1.1)
robot.push_command()
robot.wait_command() # Wait for motion to complete

# Move all three wrist motors one at a time
robot.end_of_arm.move_to('wrist_yaw', np.radians(45))
robot.push_command()
robot.wait_command()

robot.end_of_arm.move_to('wrist_pitch', np.radians(45))
robot.push_command()
robot.wait_command()

robot.end_of_arm.move_to('wrist_roll', np.radians(45))
robot.push_command()
robot.wait_command()

# Open gripper and close it
robot.end_of_arm.move_to('stretch_gripper', 50)
robot.push_command()
robot.wait_command()

# Rotate both of the motors connected to camera
robot.head.move_by('head_pan', np.radians(45)) # Move head pan
robot.head.move_by('head_tilt', np.radians(45)) # Move head tilt
robot.push_command()
robot.wait_command()

# Move back to stow position
robot.stow()
robot.push_command()
robot.wait_command()

# Drive forward 0.5m, rotate 180deg, drive 0.5m forward
robot.base.translate_by(0.2) # Move robot base 0.2 meters forward
robot.push_command()
robot.wait_command()

robot.base.rotate_by(np.radians(180)) # Rotate base by 30 degrees
robot.push_command()
robot.wait_command()

robot.base.translate_by(0.2) # Move robot base 0.2 meters forward
robot.push_command()
robot.wait_command()

