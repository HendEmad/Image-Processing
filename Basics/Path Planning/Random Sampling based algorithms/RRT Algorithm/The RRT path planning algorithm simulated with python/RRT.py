# This class contains the test use of all methods we have created in RRTbasePy class
import pygame
from RRTbasePy import RRTGraph
from RRTbasePy import RRTMap
import time

def main():
    dimensions = (600, 1000)
    start = (50, 50)
    goal = (510, 510)
    obsDim = 30
    obsNum = 50
    iteration = 0

    # In case of the algorithm got stuck and kept iterating even if the goal is found
    # Raise an exception so the planning is reinitialized

    # declare a variable t1 to hold the initial time reading
    t1 = 0

    pygame.init()
    map = RRTMap(start, goal, dimensions, obsDim, obsNum)
    graph = RRTGraph(start, goal, dimensions, obsDim, obsNum)

    # make obstacles
    obstacles = graph.makeObs()
    # draw the map
    map.drawMap(obstacles)

    t1 = time.time()
    # Create a while loop that will iterate only 500 times; to avoid the freezing of the window
    elapsed = time.time() - t1
    t1 = time.time() # Reassign the present time value to t1
    # if the elapsed time is greater than 10 seconds, we consider that to be a timeout and raise an exception
    if elapsed > 10:
        raise

    while not graph.path_to_goal():
        # assign in each iteration the difference of the past and the present values of the time to the elapsed variable
        # the program has two choices bias or expand
        # call the bias method every 10 iterations
        if iteration % 10 == 0:
            x, y, parent = graph.bias(goal)
            # draw the node and the edge created by it
            pygame.draw.circle(map.map, map.grey, (x[-1], y[-1]),
                               map.nodeRad + 2, 0)
            pygame.draw.line(map.map, map.Blue, (x[-1], y[-1]),
                             (x[parent[-1]], y[parent[-1]]), map.edgeThickness)
        else:
            # expand the tree towards random directions
            x, y, parent = graph.expand()
            # draw the node and the edge
            pygame.draw.circle(map.map, map.grey, (x[-1], y[-1]),
                               map.nodeRad + 2, 0)
            pygame.draw.line(map.map, map.Blue, (x[-1], y[-1]),
                             (x[parent[-1]], y[parent[-1]]), map.edgeThickness)

            # Update our display in a regular manner to show the animation
        if iteration % 5 == 0:
            pygame.display.update()
        # increment the iterations by one
        iteration += 1
    # draw the path after the termination of the loop
    map.drawPath(graph.getPathCoord())
    # freeze the screen when the loop is finished
    pygame.display.update()
    pygame.event.clear()
    pygame.event.wait(0)

# Exception handling to avoid errors
# If the result is true, loop terminates and if it is false, it keeps trying until the path is found
if __name__ == '__main__':
    result = False
    while not result:
        try:
            main()
            result = True
        except:
            result = False