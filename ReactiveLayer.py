from robobopy.Robobo import Robobo
from robobopy.utils.Color import Color
from robobopy.utils.IR import IR
import Global
import time

class ReactiveLayer:
    def __init__(self, roboID, ip):
        # Initialization of the robot and speed
        self.ID = roboID
        self.robot = Robobo(ip)
        self.robot.connect()
        time.sleep(1)

        self.robot.setActiveBlobs(True, True, True, True)

        self.robot.sayText("Hello")
        self.robot.movePanTo(0,5)
        self.robot.moveTiltTo(90, 5)
        time.sleep(1)

        self.base_speed = 8
        self.turn_speed = 15
        # TODO: Add current orientation, goal orientation
        # DONE
        self.current_orientation = Global.Orientation.N
        self.goal_orientation = Global.Orientation.N

    def move_forward(self):
        # moves the robot forward
        self.robot.moveWheels(self.base_speed, self.base_speed)

    def stop_robot(self):
        # Stops the robot
        self.robot.stopMotors()

    def get_ir_sensor_data(self):
        # Reads the IR sensors for obstacle detection (return a list of values for teh 8 sensors)

        data = self.robot.readAllIRSensor()
        # print("DEBUG RAW IR DATA:", data) 

        if isinstance(data, dict):
            return data
        
        manual_data = []
        for i in range(8):
            val = self.robot.readIRSensor(i)
            manual_data.append(val if val is not None else 0)
        # print("DEBUG MANUAL IR DATA:", manual_data)
        return manual_data
    
    def detect_target_robot(self):
        # Uses the camera to detect the other robot 
        try:    
            blob = self.robot.readColorBlob(Color.BLUE)

            if blob and hasattr(blob, 'size') and blob.size > 0:
                print(f"DEBUG: I see something blue! Data: {blob}")
                self.stop_robot()
                return True
        except Exception as e:
            print(f"Vision error: {e}")
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
        sensors = self.get_ir_sensor_data()
        
        if not sensors:
            return 0
        
        try:
            f_left = sensors['Front-L']
            f_center = sensors['Front-C']
            f_right = sensors['Front-R']
            
            max_front = max(f_left, f_center, f_right)

            if max_front > 500:
                print(f"Obstacle detected! Vaalue: {max_front}")
                return max_front
                
        except Exception as e:
            print(f"Error accessing sensors: {e}")
            
        return 0

    def escape_wall(self):
        
        self.robot.moveWheels(-40, -40)
        time.sleep(1.5)
        self.stop_robot()

    # TODO: 'Set goal orientation' function for mediative layer to give orientation to this robot instance
    # DONE 

    def set_goal_orientation(self, orientation):
        # Sets direction based on MediativeLaayer
        self.goal_orientation = orientation

    
    # TODO: 'Get current orientation' function for mediative layer to use to mark obstacles with
    # DONE

    def get_current_orientation(self):
        # Returns orientation for maapping
        return self.current_orientation 
    

    # TODO: 'Get Robo ID' for mediative layer to know which robot is detecting what
    # DONE

    def get_robot_id(self):
        # Returns robot id
        return self.ID
    
    def RunLayer(self):
        # TODO: Run the functions above within this funtion, since this function will be the thread that runs
        # DONE
        while not self.detect_target_robot():
            if self.current_orientation != self.goal_orientation:
                self.rotate_to_direction(self.current_orientation, self.goal_orientation)
                self.current_orientation = self.goal_orientation

            obstacle_dist = self.check_and_report_obstacle()
            if obstacle_dist > 3000:
                self.stop_robot()
                self.escape_wall()
                current_val = int(self.current_orientation.value)
                new_val = (current_val + 2) % 8 
                self.set_goal_orientation(Global.Orientation(new_val))
                self.set_goal_orientation(Global.Orientation(new_val))
                print(f"Orientation changed")
            else:
                self.move_forward()
            time.sleep(0.1)
        
        print(f"Robot {self.ID} finished task")
        self.stop_robot()

        # while (!self.detect_target_robot):
        #   if (current orientation != goal orientation):
        #      rotate_to_direction(current, goal)
        #   else
        #      self.move_forward()
