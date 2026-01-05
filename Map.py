import numpy as np
import ShortestPath

class Map:
    '''
    Map
    Description:
        This class creates a map made up of different coordinate points, using a scale of 1 cm per square

    Attributes:
        grid - A boolean numpy array of 1 x 1 cm squared spaces with false for empty spaces and true for filled spaces
        startPositions - a tuple of a tuple of coordinates for the robot starting points

    Functions:
        ToMap - Reads a text file and returns a Map object
        GetStarts - Returns the start positions of the robots
        AddObstacle - Adds an obstacle at a specific coordinate point
        DrawLine - Draws a line from point A to B, and returns a shortest path object
    '''
    def ToMap(filepath):
        '''
        ToMap function
        Input - filepath of the text file (.??? file)
        Output - Map object
        Description: Creates a Map object from the read-in coordinates
        '''
        # TODO

    def GetStarts(self)
        '''
        GetStarts function
        Output - Tuple of integer tuple
        Description: Returns the pair of coordinate pairs where the robots start in the map
        '''
        return self.startPositions

    def AddObstacle(self, coords)
        '''
        AddObstacle function
        Input - coordinates of the obstacle
        Description: Creates an object connected to the two Robobo robots, and create the map and shortest
            path calculations, called by the Mediative Layer whenever a robot detects an obstacle
        '''
        self.grid[coords[0], coords[1]] = True
        
    def DrawLine(self, roboOne, roboTwo)
        '''
        DrawLine function
        Input - coordinates of the two robots
        Output - ShortestPath object
        Description: Creates a ShortestPath object between two points, using the map and the obstacles to
            find out where the line will be
        '''
    