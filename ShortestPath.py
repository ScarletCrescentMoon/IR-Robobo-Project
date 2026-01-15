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
        AddCoords - Adds a coordinate tuple to pathCoords
        CalcOri - Calculates the orientations with pathCoords
        GetPath - Returns the pathCoords attribute
    '''
    def __init__(self, coordinates):
        self.pathCoords = []
        self.coordOne = coordinates[1]
        self.coordTwo = coordinates[2]

    def AddCoords(self, coordinatePair):
        self.pathCoords.insert(-2, coordinatePair)

    def CalcOri(self):
        oriOne = Orientation.N
        oriTwo = Orientation.N
        xOne = self.pathCoord[0][0] - self.pathCoord[1][0]
        xTwo = self.pathCoord[-2][0] - self.pathCoord[-1][0]
        yOne = self.pathCoord[0][1] - self.pathCoord[1][1]
        yTwo = self.pathCoord [-2][1] - self.pathCoord[-1][1]

        if (abs(xOne) > abs(yOne)):
            if xOne > 0:
                oriOne = Orientation.W
            elif xOne < 0:
                oriOne = Orientation.E
        if (abs(xOne) < abs(yOne)):
            if yOne > 0:
                oriOne = Orientation.N
            elif yOne < 0:
                oriOne = Orientation.S
        if (abs(xOne) == abs(yOne)):
            if xOne > 0:
                if yOne > 0:
                    oriOne = Orientation.NW
                else:
                    oriOne = Orientation.SW
            else:
                if yOne > 0:
                    oriOne = Orientation.NE
                else:
                    oriOne = Orientation.SE

        if (abs(xTwo) > abs(yTwo)):
            if xTwo > 0:
                oriTwo = Orientation.W
            elif xTwo < 0:
                oriTwo = Orientation.E
        if (abs(xTwo) < abs(yTwo)):
            if yTwo > 0:
                oriTwo = Orientation.N
            elif yTwo < 0:
                oriTwo = Orientation.S
        if (abs(xTwo) == abs(yTwo)):
            if xTwo > 0:
                if yTwo > 0:
                    oriTwo = Orientation.NW
                else:
                    oriTwo = Orientation.SW
            else:
                if yTwo > 0:
                    oriTwo = Orientation.NE
                else:
                    oriTwo = Orientation.SE
        return (oriOne, oriTwo)

    def GetPath(self):
        return self.pathCoords
        