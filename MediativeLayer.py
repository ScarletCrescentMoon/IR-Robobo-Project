from robobo.py import Robobo

import time

class MediativeLayer:
    '''
    MediativeLayer
    Description:
        This class connects the ReactiveLayer and DeliberativeLayer objects,
        functioning as a rudimentary I/O medium

    Attributes:
        roboOne, roboTwo - the robot objects to call for information
        roboOneIn, roboTwoIn - Tuple of data consisting of distance traveled and
            orientation traveled in
        obstaclesIn - list of obstacles found
        roboOneOut, roboTwoOut - Orientation of which direction the robots should travel in
        doneBool - The boolean that stops the loop running the thread loop

    Functions:
        GetRoboIn - Returns roboOneIn and roboTwoIn
        SetRoboIn - Gains the data for roboOneIn or roboTwoIn
        GetObstaclesIn - Returns the data of obstacles the robots have discovered
        SetObstaclesIn - Gains the data of obstacles the robots have discovered
        GetRoboOut - Returns the data for where the robots should head for the shortest path
        SetRoboOut - Gains the data for where the robots should head for the shortest path
        IsDone - Gets doneBool for the DeliberativeLayer to check against
        RunLayer - Function to run the layer as a thread, reactive layers as inputs
    '''

    def __init__(self):
        '''
        Initialization function
        Output - MediativeLayer object
        Description: Creates an object connected to the two Robobo robots and the DeliberativeLayer
        '''
        self.roboOneIn = None
        self.roboTwoIn = None
        self.obstaclesIn = []
        self.roboOneOut = None
        self.roboTwoOut = None
        self.doneBool = False

    def GetRoboIn(self):
        '''
        GetRoboIn function
        Output - roboOneIn, roboTwoIn: return the robot´s vector movement
        Description: Defines roboOneIn and roboTwoIn, called by RunLayer method
        '''
        vecOne = (self.roboOneIn[0], self.roboOneIn[1])
        vecTwo = (self.roboTwoIn[0], self.roboTwoIn[1])
        self.roboOneIn = None
        self.roboTwoIn = None
        return (vecOne, vecTwo)

    def SetRoboIn(self):
        '''
        SetRoboIn function
        Description: Returns roboOneIn and roboTwoIn, called by RunLayer method
        '''
        self.roboOneIn = int(self.roboOne.HowFar())
        self.roboTwoIn = int(self.roboTwo.HowFar())

    def GetObstaclesIn(self):
        '''
        GetObstaclesIn function
        Output - obstaclesIn: list of obstacles found and their coordinates
        Description: Defines obstaclesIn, called by DeterminitiveLayer
        '''
        obsList = self.obstaclesIn.copy()
        self.obstaclesIn = []
        return obsList

    def SetObstaclesIn(self):
        '''
        SetObstaclesIn function
        Description: Defines obstaclesIn, called by RunLayer method
        '''
        distObst = (self.roboOne.check_and_report_obstacle(), self.roboTwo.check_and_report_obstacle())
        for obst in distObst:
            if obst != 0:
                #TODO: Calc distance in cm and append to obstaclesIn
        

    def SetRoboOut(self, orientations):
        '''
        SetRoboOut function
        Input - orientations: tuple of orientations for each bot to turn to
        Description: Changes the robot goal orientations, run by DeterminitiveLayer
        '''
        self.roboOneOut = orientations[0]
        self.roboTwoOut = orientations[1]
        self.roboOne.set_goal_orientation(self.roboOneOut)
        self.roboTwo.set_goal_orientation(self.roboTwoOut)

    def IsDone(self):
        return self.doneBool

    def RunLayer(self, robot1, robot2):
        self.roboOne = robot1
        self.roboTwo = robot2
        while not self.IsDone():
            time.sleep(0.2)
            
            self.SetRoboIn()
            self.SetObstaclesIn()
            
            if self.roboOne.IsDone() and self.roboTwo.isDone():
                self.doneBool = True
