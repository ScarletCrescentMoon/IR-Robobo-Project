from ReactiveLayer import ReactiveLayer
import time
import Global

def test_robot():
    ip_robot = "192.168.1.87"
    reactive_layer = ReactiveLayer(ip_robot)
    reactive_layer.base_speed = 8
    
    current_dir = Global.Orientation.N
    
    THRESHOLD = 340000

    time.sleep(3)

    attempts = 0
    while attempts < 20:
        val = reactive_layer.robot.readIRSensor(3)
        if val is not None:
            break
        time.sleep(0.5)
        attempts += 1

    while True:
        sensors = reactive_layer.get_ir_sensor_data()
        if sensors and len(sensors) > 0:
            break
        time.sleep(0.2)

    print("Test strats: moving forward")
    reactive_layer.move_forward()
    
    try:
        while True:
            if reactive_layer.detect_target_robot():
                print("Target detected! Stopping.")
                break

            sensors = reactive_layer.get_ir_sensor_data()

            if not sensors or len(sensors) == 0:
                center_val, left_val, right_val = 0, 0, 0
            elif isinstance(sensors, dict):
                center_val = sensors.get('Front-C', 0)
                left_val = sensors.get('Front-L', 0)
                right_val = sensors.get('Front-R', 0)
            else:

                center_val = sensors[3]
                left_val = sensors[2]
                right_val = sensors[4]

            if center_val > THRESHOLD:
                print(f"Obstacle detected: {center_val}")
                reactive_layer.stop_robot()
                time.sleep(0.2)

                reactive_layer.robot.moveWheels(-30, -30)
                time.sleep(1.2)
                reactive_layer.stop_robot()
                time.sleep(0.2)

                if left_val < right_val:
                    new_dir_val = (current_dir.value + 2) % 8
                else:
                    new_dir_val = (current_dir.value - 2) % 8

                target_dir = Global.Orientation(new_dir_val)
                reactive_layer.rotate_to_direction(current_dir, target_dir)
                current_dir = target_dir

                time.sleep(0.2)
                reactive_layer.move_forward()
            
            time.sleep(0.05)

    except KeyboardInterrupt:
        reactive_layer.stop_robot()
        print("Test stopped")

if __name__ == "__main__":
    test_robot()