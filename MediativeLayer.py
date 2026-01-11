from robobo.py import Robobo

class MediativeLayer:
    '''
    MediativeLayer
    Description:
        This class connects the ReactiveLayer and DeliberativeLayer objects,
        functioning as a rudimentary I/O medium

    Attributes:
        roboOneIn, roboTwoIn - Tuple of data consisting of distance traveled and
            orientation traveled in
        obstaclesIn - list of obstacles found
        roboOneOut, roboTwoOut - Orientation of which direction the robots should travel in
        doneBool - The boolean that stops the loop running the thread loop

    Functions:
        GetRoboIn - Gains the data for roboOneIn or roboTwoIn
        GetObstaclesIn - Gains the data of obstacles the robots have discovered
        GetRoboOut - Gains the data for where the robots should head for the shortest path
        CalculateOuts - Uses current data to calculate the output data from input data
        Finish - Sets doneBool to True
        IsDone - Gets doneBool for the DeliberativeLayer to check against
        RunLayer - Function to run the layer as a thread
    '''

    def __init__(self):
        '''
        Initialization function
        Output - MediativeLayer object
        Description: Creates an object connected to the two Robobo robots and the DeliberativeLayer
        '''
        self.roboOneIn = 0
        self.roboTwoIn = 0
        self.obstaclesIn = []
        self.roboOneOut = 0
        self.roboTwoOut = 0
        self.doneBool = False
