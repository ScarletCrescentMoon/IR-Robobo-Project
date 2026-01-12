import Global
from ReactiveLayer import ReactiveLayer
import time

def debug_reactive_layer():
    # 1. Initialization and ID Test
    layer = ReactiveLayer(roboID=1, ip="127.0.0.1")
    
    # Force detection to False to test movement and obstacle logic indefinitely
    layer.detect_target_robot = lambda: False

    print(f"DEBUG: Testing get_robot_id: {layer.get_robot_id()}")

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

    # 4. Manual Rotation Test
    print("DEBUG: Testing rotation to goal")
    layer.rotate_to_direction(layer.current_orientation, layer.goal_orientation)
    layer.current_orientation = layer.goal_orientation
    print(f"DEBUG: Orientation after rotation: {layer.get_current_orientation()}")

    # 5. RunLayer Test (Movement + Escape Logic)
    print("DEBUG: Starting RunLayer. Robot will move and avoid walls.")
    try:
        layer.RunLayer()
    except KeyboardInterrupt:
        layer.stop_robot()
        print("DEBUG: Test stopped by user")

if __name__ == "__main__":
    debug_reactive_layer()