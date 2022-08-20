# This class contains all the methods we will use
import random
import pygame
import math


# Class contains methods for DRAWING the map, obstacles and the actual path that was calculated
class RRTMap:
    def __init__(self, start, goal, mapDim, obsDim, obsNum):
        # Declare variables
        self.start = start
        self.goal = goal
        self.mapDim = mapDim  # height, width
        self.mapH, self.mapW = self.mapDim

        # Window settings
        # Create window name
        self.mapWindowName = 'RRT Path Planning'
        pygame.display.set_caption(self.mapWindowName)
        # Draw the map
        self.map = pygame.display.set_mode((self.mapW, self.mapH))
        # set window color
        self.map.fill((255, 255, 255))  # white
        # variables for drawing nodes and edges
        self.nodeRad = 5  # node radius
        self.nodeThickness = 0  # node thickness
        self.edgeThickness = 1  # edge thickness

        self.obstacles = []  # list of obstacles
        self.obsDim = obsDim  # Obstacles dimensions
        self.obsNum = obsNum  # Obstacles number

        # Colors
        self.grey = (70, 70, 70)
        self.Blue = (0, 0, 255)
        self.Green = (0, 255, 0)
        self.Red = (255, 0, 0)
        self.white = (255, 255, 255)

    # Draw the map
    # draw the start and goal as circles
    def drawMap(self, obstacles):
        # thickness = 0 to draw a solid circle
        pygame.draw.circle(self.map, self.Green, self.start, self.nodeRad + 5,
                           0)  # start circle, 0 indicates to the thickness
        # the goal circle is wider and the thickness is one to draw an empty circle
        pygame.draw.circle(self.map, self.Green, self.goal, self.nodeRad + 20, 1)
        # draw the obstacles
        self.drawObs(obstacles)

    # Draw the path would be calculated
    def drawPath(self, path):
        for node in path:
            pygame.draw.circle(self.map, self.Red, node, self.nodeRad+3, 0)

    # The obstacles, it takes the obstacles as input to draw them
    def drawObs(self, obstacles):
        obstaclesList = obstacles.copy()
        while len(obstaclesList) > 0:
            # pop the obstacle from the list
            obstacle = obstaclesList.pop(0)
            # draw the popped obstacles in the screen
            pygame.draw.rect(self.map, self.grey, obstacle)  # Map is the environment to draw thw obstacles on


class RRTGraph:
    def __init__(self, start, goal, mapDim, obsDim, obsNum):
        (x, y) = start
        self.start = start
        self.goal = goal
        self.goalFlag = False  # true if th e tree reaches the goal region
        self.mapH, self.mapW = mapDim  # Separate height and width
        # Represent the tree
        self.x = []
        self.y = []
        self.parent = []
        self.x.append(x)
        self.y.append(y)
        self.parent.append(0)
        # draw the obstacles
        self.obstacles = []
        self.obsDim = obsDim
        self.obsNum = obsNum
        # Path
        self.goalState = None  # Indicate whether the tree reached goal region or not
        self.path = []  # list to hold our calculated path

    # function to generate random x and y coordinates to represent the upper left corner of a rectangle
    def makeRandonRect(self):
        # We will subtract map width and height from obstacle dimension to make sure that the full obstacle is inside the rectangle
        # random.uniform --> generates a number between two input values
        upperCornerX = int(random.uniform(0, self.mapW - self.obsDim))
        upperCornerY = int(random.uniform(0, self.mapH - self.obsDim))
        # return a tuple of the coordinates
        return upperCornerX, upperCornerY

    # create the obstacles and store them in a list
    def makeObs(self):
        obs = []
        for i in range(0, self.obsNum):
            rectang = None  # Hold the obstacles temporarily before it gets stored
            startGoalCol = True  # flag indicates whether the start and goal positions in the map are inside a newly created obstacle
            while startGoalCol:
                upper = self.makeRandonRect()
                rectang = pygame.Rect(upper, (self.obsDim, self.obsDim))
                # use collidepoint() method to test is the created list
                if rectang.collidepoint(self.start) or rectang.collidepoint(self.goal):
                    startGoalCol = True
                else:
                    startGoalCol = False
            # While the start and goal positions collide with the obstacle coordinates, loop
            # else, terminate. Then. append the obstacle
            # This is done to be sure that the start or goal circles are outside all obstacles
            obs.append(rectang)
        self.obstacles = obs.copy()
        return obs

    # This function add random nodes based on random samples
    def addNode(self, n, x, y):  # Identification number of the node(index), its x and y coordinates
        # insert x
        self.x.insert(n, x)
        self.y.append(y)

    def removeNode(self, n):
        self.x.pop(n)
        self.y.pop(n)

    def addEdge(self, parent, child):
        self.parent.insert(child, parent)  # child as index and parent is stored as element

    def removeEdge(self, n):
        self.parent.pop(n)  # this will cut the relationship between the parent and the child nodes

    # this function is needed of we want to extract the latest node or find the number of nodes
    def numberOfNodes(self):
        return len(self.x)

    # to measure the distance between two nodes
    def distance(self, n1, n2):
        (x1, y1) = (self.x[n1], self.y[n1])
        (x2, y2) = (self.x[n2], self.y[n2])
        # calculate the distance
        px = (float(x1) - float(x2)) ** 2
        py = (float(y1) - float(y2)) ** 2
        return (px + py) ** 0.5

    # this function generates random samples from the map
    def sample_envir(self):
        x = int(random.uniform(0, self.mapW))
        y = int(random.uniform(0, self.mapH))
        return x, y

    # This function takes the new added node that was sampled from the environment
    # and measured the distance to every node in the tree
    def nearestNeighbour(self, n):
        dmin = self.distance(0, n)
        nnear = 0  # It holds the id of the closest node we found so far
        for i in range(0, n):
            if self.distance(i, n) < dmin:
                dmin = self.distance(i, n)
                nnear = i
        return nnear

    # This function is to create a new node between the new node and the nearest node
    def step(self, nnear, nrand, dmax=35):
        d = self.distance(nnear, nrand)  # measure the distance between nnear and nrand
        if d > dmax:
            u = dmax / d
            # extract (x, y) coordinates of nnear
            (xnear, ynear) = (self.x[nnear], self.y[nnear])
            # extract (x, y) coordinates of nrand
            (xrand, yrand) = (self.x[nrand], self.y[nrand])
            (px, py) = (xrand - xnear, yrand - ynear)
            # angle calculation by providing py and px to arctan2
            theta = math.atan2(py, px)
            # new node coordinates
            (x, y) = (int(xnear + dmax * math.cos(theta)),
                      int(ynear + dmax * math.sin(theta)))
            # remove nrand
            self.removeNode(nrand)
            # check if the new node created is inside the goal region of raduis 35
            if abs(x - self.goal[0]) < dmax and abs(y - self.goal[1]) < dmax:
                # This condition checks whether the goal is close enough to the tree
                # if true, we found the goal and there is no need for adding the new calculated the new calculated node to the tree
                # instead, we will add the goal itself in its place
                self.addNode(nrand, self.goal[0], self.goal[1])
                # declare the nrand id as the id of the goal state
                # and get the goal flag to true
                self.goalState = nrand
                self.goalFlag = True
            else:
                # add the new calculated node to the tree
                self.addNode(nrand, x, y)

    # this function checks if the new node will be added is in a free space or not
    def isFree(self):
        n = self.numberOfNodes() - 1
        (x, y) = (self.x[n], self.y[n])
        obs = self.obstacles.copy()
        # test the node
        while len(obs) > 0:
            rectang = obs.pop(0)
            if rectang.collidepoint(x, y):
                # remove the node from the tree
                self.removeNode(n)
                return False  # the node is not free
        return True

    # This function check if the edge crosses any obstacles
    def crossObstacles(self, x1, x2, y1, y2):
        obs = self.obstacles.copy()
        while len(obs) > 0:
            rectang = obs.pop(0)
            # To test a line(edge) for collision, we can use interpolation to
            # Create intermediate checkpoints between the two nodes, and check if anyone of them collide with the obstacles
            for i in range(0, 101):
                u = i / 100  # used in generating the checkpoints
                x = x1 * u + x2 * (1 - u)
                y = y1 * u + y2 * (1 - u)
                # if the current obstacle which is held in rectang collides with the ith checkpoint
                if rectang.collidepoint(x, y):
                    return True
        return False

    # Function to connect two nodes
    def connectNodes(self, n1, n2):
        (x1, y1) = (self.x[n1], self.y[n1])
        (x2, y2) = (self.x[n2], self.y[n2])
        # Check if the connection edge between them crossed any obstacles or not
        if self.crossObstacles(x1, x2, y1, y2):
            # if crossed, remove node 2
            self.removeNode(n2)
            return False
        else:
            self.addEdge(n1, n2)  # Add n1 as a parent and n2 as a child
            return True

    # The two main behaviours of the algorithm
    # If we execute 100 iteration of this algorithm, 90% of these iterations must be expansion and 10% must be biasing; this ratio can be changed

    # Function for the random expansion of the tree using random samples
    # 2nd
    def expand(self):
        # generate new index
        n = self.numberOfNodes()
        # create the random node
        x, y = self.sample_envir()
        # add the random node to the tree temporarily
        self.addNode(n, x, y)
        # check if the created random node is in free space
        if self.isFree():
            # if true, get the nearest node to it
            xnearest = self.nearestNeighbour(n)
            # take a step from xnearest and create a new node
            self.step(xnearest, n)
            # connect the node created by step to the nearest node
            self.connectNodes(xnearest, n)
            # return the tree for other uses
        return self.x, self.y, self.parent

    # Expansion in the direction of the goal using the goal in the place of random sample
    # This will make the search process much faster
    # 1st one
    def bias(self, ngoal):
        # Generating a new index to be used in creating a new node
        n = self.numberOfNodes()
        # add the goal to the tree temporarily
        self.addNode(n, ngoal[0], ngoal[1])
        # get the nearest node in the tree to the goal
        nnear = self.nearestNeighbour(n)
        # create a permanent node and add it to the tree between the nearest node and the goal node
        # Then, remove the goal node from the tree
        self.step(nnear, n)
        # connect the newly created node to the nnear by creating an edge between them
        self.connectNodes(nnear, n)
        return self.x, self.y, self.parent

    # Function to extract the node to get the path
    # In this function, we just get the parent of every node moving backwards from the goal node to the start node
    def path_to_goal(self):
        # check if the path was actually found
        if self.goalFlag:
            # declare an empty list to hold the path nodes
            self.path = []
            # Append the goal as the first element of this list
            self.path.append(self.goalState)
            # Assign the goal parent as the next element to be added
            newPos = self.parent[self.goalState]
            # loop extracting the nodes parent and adding them to the list
            # and then the parent of the parent, until we hit the start node
            while newPos != 0:
                self.path.append(newPos)
                newPos = self.parent[newPos]
            # add it to the list as the last element
            self.path.append(0)  # Append must be in after the while loop is terminated
        return self.goalFlag

    # Function to extract the path nodes whenever we need them
    def getPathCoord(self):
        pathCoords = []
        for node in self.path:
            x, y = (self.x[node], self.y[node])
            pathCoords.append((x, y))
        return pathCoords