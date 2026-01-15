import Global
from ReactiveLayer import ReactiveLayer
import time

def debug_reactive_layer():
    # 1. Initialization and ID Test
    layer = ReactiveLayer(roboID=1, ip="192.168.1.87")
    
    # Force detection to False to test movement and obstacle logic indefinitely
    layer.detect_target_robot = lambda: False

    print(f"DEBUG: Testing get_robot_id: {layer.get_robot_id()}")

    # Test HowFar

    print("\n Test: HowFar at starting")
    dist, ori = layer.HowFar()
    print(f"DEBUG: Distance should be close to 0: {dist:.2f} cm, Orientation: {ori}")

    # 2. Orientation Tests (get/set)
    print(f"DEBUG: Initial orientation: {layer.get_current_orientation()}")
    
    layer.set_goal_orientation(Global.Orientation.E)
    print(f"DEBUG: Goal orientation set to East")

    # 3. Obstacle Detection Test (check_and_report_obstacle)
    print("DEBUG: Testing sensors. Move the robot toward a wall in RoboboSim.")
    for i in range(5):
        val = layer.check_and_report_obstacle()
        print(f"DEBUG: IR Sensor Check {i+1}: {val}")
        time.sleep(1)

    # Test HowFar while mooving
    print("\n Test: HowFar while moving")
    print("Robot moves forward for 2 seconds")
    layer.move_forward()
    time.sleep(2)
    layer.stop_robot()

    dist, ori = layer.HowFar()
    print(f"DEBUG: Distance result: {dist:.2f} cm to orientation {ori}")

    # 4. Manual Rotation Test
    print("DEBUG: Testing rotation to goal")
    layer.rotate_to_direction(layer.current_orientation, layer.goal_orientation)
    layer.current_orientation = layer.goal_orientation
    print(f"DEBUG: Orientation after rotation: {layer.get_current_orientation()}")

    # Test HowFar - at rotation distance should be 0
    dist_rot, ori_rot = layer.HowFar()
    print(f"DEBUG: After rotation, distance {dist_rot:.2f} cm, new orientation: {ori_rot}")

    # 5. RunLayer Test (Movement + Escape Logic)
    print("DEBUG: Starting RunLayer. Robot will move and avoid walls.")
    try:
        layer.RunLayer()
    except KeyboardInterrupt:
        layer.stop_robot()
        # Test HowFar
        final_dist, _ = layer.HowFar()
        print(f"\nDEBUG: Final distance: {final_dist:.2f} cm")
        print("DEBUG: Test stopped by user")

if __name__ == "__main__":
    debug_reactive_layer()