import hello_helpers.hello_misc as hm
import numpy as np

node = hm.HelloNode.quick_create('temp')
# node.move_to_pose({'joint_lift': 0.4}, blocking=True)
# node.move_to_pose({'joint_wrist_yaw': 0.0, 'joint_wrist_roll': 0.0}, blocking=True)

# Move to stow position
node.stow_the_robot()

# Extend arm and lift to full extension
node.move_to_pose({'joint_arm': 0.5, 'joint_lift': 1.1}, blocking=True)

# Move all three wrist motors one at a time
node.move_to_pose({'joint_wrist_yaw': np.radians(45)}, blocking=True)
node.move_to_pose({'joint_wrist_pitch': np.radians(45)}, blocking=True)
node.move_to_pose({'joint_wrist_roll': np.radians(45)}, blocking=True)

# Open gripper and close it
node.move_to_pose({'joint_gripper_finger_left': np.radians(50)}, blocking=True)
node.move_to_pose({'joint_gripper_finger_left': np.radians(-50)}, blocking=True)

# Rotate both of the motors connected to camera
 # Move head pan
node.move_to_pose({'joint_head_pan': np.radians(45)}, blocking=True)

 # Move head tilt
node.move_to_pose({'joint_head_tilt': np.radians(45)}, blocking=True)

# Move back to stow position
node.stow_the_robot()

# Drive forward 0.5m, rotate 180deg, drive 0.5m forward
 # Move robot base 0.2 meters forward
node.move_to_pose({'translate_mobile_base': 0.5}, blocking=True)

 # Rotate base by 30 degrees
node.move_to_pose({'rotate_mobile_base': np.radians(180)}, blocking=True)

 # Move robot base 0.2 meters forward
node.move_to_pose({'translate_mobile_base': 0.5}, blocking=True)
