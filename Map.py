import numpy as np
import ShortestPath
import math

class Map:
    '''
    Map
    Description:
        This class creates a map made up of different coordinate points, using a scale of 1 cm per square

    Attributes:
        grid - A boolean numpy array of 1 x 1 cm squared spaces with false for empty spaces and true for filled spaces
        gridWidth - maximum X value
        gridHeight - maximum Y value
        startPositions - a tuple of a tuple of coordinates for the robot starting points

    Functions:
        ToMap - Reads a text file and returns a Map object
        GetStarts - Returns the start positions of the robots
        AddObstacle - Adds an obstacle at a specific coordinate point
        GetAdj - Uses orientation and coordinate input to find an adjacent space
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

    def GetStarts(self):
        '''
        GetStarts function
        Output - Tuple of integer tuple
        Description: Returns the pair of coordinate pairs where the robots start in the map
        '''
        return self.startPositions

    def AddObstacle(self, coords):
        '''
        AddObstacle function
        Input - coordinates of the obstacle
        Description: Creates an object connected to the two Robobo robots, and create the map and shortest
            path calculations, called by the Mediative Layer whenever a robot detects an obstacle
        '''
        self.grid[coords[0], coords[1]] = True
        
    def GetAdj(self, inCoord, ori):
        '''
        GetAdj function
        Input - inCoord as coordinate inputs, ori as orientation
        Output - coordinates of the spot
        Description: Finds the coordinates of the next space in the direction specified
        '''
        if ori == Orientation.N:
            return (inCoord[0], inCoord[1] + 1)
        elif ori == Orientation.NE:
            return (inCoord[0] + 1, inCoord[1] + 1)
        elif ori == Orientation.E:
            return (inCoord[0] + 1, inCoord[1])
        elif ori == Orientation.SE:
            return (inCoord[0] + 1, inCoord[1] - 1)
        elif ori == Orientation.S:
            return (inCoord[0], inCoord[1] - 1)
        elif ori == Orientation.SW:
            return (inCoord[0] - 1, inCoord[1] - 1)
        elif ori == Orientation.W:
            return (inCoord[0] - 1, inCoord[1])
        elif ori == Orientation.NW:
            return (inCoord[0] - 1, inCoord[1] + 1)
    
    def DrawLine(self, roboOne, roboTwo):
        '''
        DrawLine function
        Input - coordinates of the two robots
        Output - ShortestPath object
        Description: Creates a ShortestPath object between two points, using the map and the obstacles to
            find out where the line will be
        '''
        frontier = []
        visited = []
        cost = 0
        prev = roboOne

        frontier.append((roboOne, cost))

        # Use cost path heuristics to determine the viable spaces to visit
        while prev[0] != roboTwo[0] and prev[1] != roboTwo[1]:
            if cost < frontier[0][1]:
                cost += 1
            prev = frontier.pop(0)
            visited.append(prev)
            for ori in range(0, Orientation.count):
                nextCoord = self.GetAdj(prev, ori)

                if nextCoord[0] == roboTwo[0] and nextCoord[1] == roboTwo[1]:
                    prev = roboTwo
                    visited.append((nextCoord), cost + 1)
                    break
                elif nextCoord[0] < self.gridWidth and nextCoord[1] < self.gridHeight and not self.grid[nextCoord[0]][nextCoord[1]]:
                    frontier.append(nextCoord, cost + 1)
                    for coord in frontier:
                        if coord[0][0] == nextCoord[0] and coord[0][1] == nextCoord[1]:
                            frontier.pop()
                            break
                    for coord in visited:
                        if coord[0][0] == nextCoord[0] and coord[0][1] == nextCoord[1]:
                            frontier.pop()
                            break
        # Remove all nodes that do not form part of the path
        out = ShortestPath.ShortestPath(roboOne, roboTwo)
        nodeFound = False
        while cost > 0:
            for coord in visited:
                for ori in range(0, Orientation.count):
                    nextCoord = self.GetAdj(prev, ori)
                    if coord[1] == cost -1 and coord[0][0] == nextCoord[0] and coord[0][1] == nextCoord[1]:
                        out.AddCoords(nextCoord)
                        nodeFoun = True
                        break
                if nodeFound:
                    break
            cost -= 1

        return out
    