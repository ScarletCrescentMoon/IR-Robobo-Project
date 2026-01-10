import Global

class ShortestPath:
    '''
    ShortestPath
    Description:
        This class draws the shortest path between two coordinates, saving it in an object with orientations for where
        robots should face to follow the path

    Attributes:
        pathCoords - A list of coordinates that contain every space in the path between two coordinates
        coordOne - start point for the path, first coordinate in pathCoords
        coordTwo - end point for the path, last coordinate in pathCoords
        orientations - orientations for robots at the start and end point, using Orientation Enums

    Functions:
        AddCoords - Adds a path object to pathCoords and update coordinates
        GetPath - Returns the pathCoords attribute
        GetOrientations - Returns orientations as an Orientation Enum
    '''
    def __init__(self):
        pass
