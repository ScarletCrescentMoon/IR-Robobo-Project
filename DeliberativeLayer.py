from robobopy.Robobo import Robobo
import Map

import time

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
        RunLayer - Function that opreates as a thread, mediative layer input
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

    def GetCoords(self):
        vecs = self.mediativeLayer.GetRoboIn()
        obstacles = self.mediativeLayer.GetObstaclesIn()

        if vecs[0][1] == Orientation.N:
            self.roboCoord_One[1] += vecs[0][0]
        elif vecs[0][1] == Orientation.NE:
            self.roboCoord_One[0] += vecs[0][0]
            self.roboCoord_One[1] += vecs[0][0]
        elif vecs[0][1] == Orientation.E:
            self.roboCoord_One[0] += vecs[0][0]
        elif vecs[0][1] == Orientation.SE:
            self.roboCoord_One[0] += vecs[0][0]
            self.roboCoord_One[1] -= vecs[0][0]
        elif vecs[0][1] == Orientation.S:
            self.roboCoord_One[1] -= vecs[0][0]
        elif vecs[0][1] == Orientation.SW:
            self.roboCoord_One[0] -= vecs[0][0]
            self.roboCoord_One[1] -= vecs[0][0]
        elif vecs[0][1] == Orientation.W:
            self.roboCoord_One[0] -= vecs[0][0]
        else:
            self.roboCoord_One[0] -= vecs[0][0]
            self.roboCoord_One[1] += vecs[0][0]

        if vecs[1][1] == Orientation.N:
            self.roboCoord_Two[1] += vecs[1][0]
        elif vecs[1][1] == Orientation.NE:
            self.roboCoord_Two[0] += vecs[1][0]
            self.roboCoord_Two[1] += vecs[1][0]
        elif vecs[1][1] == Orientation.E:
            self.roboCoord_Two[0] += vecs[1][0]
        elif vecs[1][1] == Orientation.SE:
            self.roboCoord_Two[0] += vecs[1][0]
            self.roboCoord_Two[1] -= vecs[1][0]
        elif vecs[1][1] == Orientation.S:
            self.roboCoord_Two[1] -= vecs[1][0]
        elif vecs[1][1] == Orientation.SW:
            self.roboCoord_Two[0] -= vecs[1][0]
            self.roboCoord_Two[1] -= vecs[1][0]
        elif vecs[1][1] == Orientation.W:
            self.roboCoord_Two[0] -= vecs[1][0]
        else:
            self.roboCoord_Two[0] -= vecs[1][0]
            self.roboCoord_Two[1] += vecs[1][0]

        for obstacle in obstacles:
            self.map.AddObstacle(obstacle)

    def CalcPath(self):
        self.shortestPath = self.map.DrawLine(self.roboCoord_One, self.roboCoord_Two)

    def RunLayer(self, medLayer):
        self.mediativeLayer = medLayer
        while not self.mediativeLayer.isDone():
            time.sleep(0.1)
            self.GetCoords()
            self.CalcPath()

            oris = self.shortestPath.CalcOri()
            self.mediativeLayer.SetRoboOut(oris)
