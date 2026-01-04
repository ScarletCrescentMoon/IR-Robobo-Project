from robobopy.Robobo import Robobo
import Map

class DefinitiveLayer:
    '''
    DefinitiveLayer
    Description:
        This class creates a definitive layer for the robots, running in a thread alongside the two robots
        and the Mediative Layer.

    Attributes:
        Map - Map object of the maze
        ShortestPath - The shortest path as an object
        RoboCoord_One - The coordinates of the first robot
        RoboCoord_Two - The coordinates of the second robot
        MediativeLayer - The Mediative Layer object

    Functions:
        GetCoords - Get coordinates from the Mediative Layer object
        CalcPath - Caclulates the shortest path between two robots
    '''
    def __init__(self, Robobo roboOne, Robobo roboTwo):
        '''
        Initialization function
        Input - Robobo, Robobo: The two robots that are functioning on Reactive Layers
        Output - DefinitiveLayer object
        Description: Creates an object connected to the two Robobo robots, and create the map and shortest path calculations
        '''
