from robobopy.Robobo import Robobo
import Global
import time

class ReactiveLayer:
    def __init__(self, ip):
        # Initialization of the robot and speed

        self.robot = Robobo(ip)
        self.robot.connect()
        time.sleep(1)
        self.robot.sayText("Hello")
        self.robot.movePanTo(0,5)
        self.base_speed = 12
        self.turn_speed = 15

    def move_forward(self):
        # moves the robot forward
        self.robot.moveWheels(self.base_speed, self.base_speed)

    def stop_robot(self):
        # Stops the robot
        self.robot.stopMotors()

    def get_ir_sensor_data(self):
        # Reads the IR sensors for obstacle detection (return a list of values for teh 8 sensors)

        data = self.robot.readAllIRSensor()
        if not data or len(data) == 0:
            try:
                manual_data = []
                for i in range(8):
                    val = self.robot.readIRSensor(i)
                    manual_data.append(val if val is not None else 0)
                return manual_data
            except:
                return []

        return data
    
    def detect_target_robot(self):
        # Uses the camera to detect the other robot 
        try:    
            blob = self.robot.readColorBlob('red')

            if blob and (isinstance(blob, list) and len(blob) > 0 or not isinstance(blob, list)):
                self.stop_robot()
                return True
        except:
            pass
        return False
    
    def rotate_to_direction(self, current_orientation=None, target_orientation=None):
        # Rotates the robot to the correct orientation (based on the Enum from Gloabl.py)

        if current_orientation is None or target_orientation is None:
            print("No orientation provided, performing default 90-degree turn")
            self.robot.moveWheels(self.turn_speed, -self.turn_speed)
            time.sleep(1.2)
            self.stop_robot()
            return
        
        try: 
            val_target = int(target_orientation.value)
            val_current = int(current_orientation.value)

        except AttributeError:
            val_target = int(target_orientation)
            val_current = int(current_orientation)

        diff = (val_target - val_current) % 8

        if diff == 0: 
            return
        
        print(f"Rotate to: {target_orientation}")

        rotation_time = diff * 0.6
        if diff <= 4:
            self.robot.moveWheels(self.turn_speed, -self.turn_speed)
        else:
            rotation_time = (8 - diff) * 0.6
            self.robot.moveWheels(-self.turn_speed, self.turn_speed)

        time.sleep(rotation_time)
        self.stop_robot()
    
    def check_and_report_obstacle(self):
        # Checks the sensors and return true if there is a wall in front of the robot

        sensors = self.get_ir_sensor_data()
        if not sensors:
            return False
        
        if isinstance(sensors, dict):
            front_val = sensors.get('Front-C', 0)
        else:
            front_val = sensors[3] if len(sensors) > 3 else 0

        if front_val > 400000:
            print(f"Obstacle detected ({front_val})")
            return True
        
        return False

    def escape_wall(self):
        
        self.robot.moveWheels(-40, -40)
        time.sleep(1.5)
        self.stop_robot()
