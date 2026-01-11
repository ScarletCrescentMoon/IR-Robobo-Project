from robobopy.Robobo import Robobo
import Map

class DeliberativeLayer:
    '''
    DeliberativeLayer
    Description:
        This class creates a definitive layer for the robots, running in a thread alongside the two robots
        and the Mediative Layer.

    Attributes:
        map - Map object of the maze
        shortestPath - The shortest path as an object
        roboCoord_One - The coordinates of the first robot
        roboCoord_Two - The coordinates of the second robot
        mediativeLayer - The Mediative Layer object of which to reference

    Functions:
        GetCoords - Get coordinates from the Mediative Layer object
        CalcPath - Caclulates the shortest path between two robots
        RunLayer - Function that opreates as a thread
    '''
    def __init__(self, mapFile):
        '''
        Initialization function
        Input - mapFile: filepath string for the map object initialization
        Output - DefinitiveLayer object
        Description: Creates an object connected to the two Robobo robots, and create the map and shortest path calculations
        '''
        self.map = Map.ToMap(mapFile)
        coords = self.map.GetStarts()
        self.roboCoord_One = coords[0]
        self.roboCoord_Two = coords[1]
