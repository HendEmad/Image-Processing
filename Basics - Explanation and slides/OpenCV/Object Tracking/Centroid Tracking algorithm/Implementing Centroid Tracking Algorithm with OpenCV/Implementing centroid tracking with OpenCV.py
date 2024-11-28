# Import the necessary packages
from scipy.spatial import distance as dist
from collections import OrderedDict
import numpy as np


class CentroidTracker:
    def __init__(self, maxDisappeared=50):
        # Initialize the next unique object ID along with two ordered dictionaries used to keep track of mapping a given object ID to its centroid and number
        # of consecutive frames it has been marked as disappeared, respectively
        self.nextObjectID = 0
        self.objects = OrderedDict()
        self.disappeared = OrderedDict()

        # Store the number of maximum consecutive frames a given object is allowed to be marked as disappeared until we need to deRegister the object from tracking
        self.maxDisappeared = maxDisappeared

    # Method responsible for adding new objects to our tracker
    def register(self, centroid):
        # When registering an object, we use the next available object ID to store the centroid
        self.objects[self.nextObjectID] = centroid
        self.disappeared[self.nextObjectID] = 0
        self.nextObjectID += 1

    # Method for removing objects from out tracker
    def deRegister(self, objectID):
        # To deRegister an object ID, we delete the object ID from both of our respective dictionaries
        del self.objects[objectID]
        del self.disappeared[objectID]

    # Update the tracker coordinate positions
    def update(self, rects):
        # Check if the list of input bounding box rectangles is empty
        if len(rects) == 0:
            # Loop over any existing tracked objects and mark them as disappeared
            for objectID in list(self.disappeared.keys()):
                self.disappeared[objectID] += 1

                # If we have reached a maximum number of consecutive frames where a given object has been marked as missing, deRegister it
                if self.disappeared[objectID] > self.maxDisappeared:
                    self.deRegister(objectID)

            # Return early as there are no centroids or tracking info to update
            return self.objects

        # Initialize numpy array of input centroids for the current frame
        inputCentroids = np.zeros((len(rects), 2), dtype="int")

        # Loop over the bounding box rectangles
        for (i, (startX, startY, endX, endY)) in enumerate(rects):
            # use the bounding box coordinates to drive the centroid
            cX = int((startX + endX) / 2.0)
            cY = int((startY + endY) / 2.0)
            inputCentroids[i] = (cX, cY)

        # If we are currently not tracking any objects, take the input centroids and register each of them
        if len(self.objects) == 0:
            for i in range(len(inputCentroids)):
                self.register(inputCentroids[i])
        # Otherwise, we are currently tracking objects, so we need to try to match the input centroids to existing object centroids
        else:
            # Grab the set of objects IDs and corresponding centroids
            objectIDs = list(self.objects.keys())
            objectCentroids = list(self.objects.values())

            # Compute the distance between each pair of object centroids and input centroids, respectively
            # Our goal will be to match an input centroid to an existing object centroid
            D = dist.cdist(np.array(objectCentroids), inputCentroids)

            # In order to perform this matching, we must:
            # 1. find the smallest values in each row.
            # 2. sort the row indices based on their in ascending order
            rows = D.min(axis=1).argsort()

            # next, we perform a similar process on the columns by finding the smallest value in each column and then sorting using the previously computed row index list
            cols = D.argmin(axis=1)[rows]

            # In order to determine if we need to update, register, or deRegister an object we need to keep track of which of the rows and columns indexes
            # we have already examined
            usedRows = set()
            usedCols = set()

            # loop over the combination of the (row, column) index tuples
            for (row, col) in zip(rows, cols):
                # if we have already examined either the row or column value before, ignore it
                if row in usedRows or col in usedCols:
                    continue
                # otherwise:
                # 1. Grab the object ID for the current row
                # 2. Set its new centroid
                # 3. Reset the disappeared counter
                objectID = objectIDs[row]
                self.objects[objectID] = inputCentroids[col]
                self.disappeared[objectID] = 0

                # Indicate that we have examined each of the row and colum indices, respectively
                usedRows.add(row)
                usedCols.add(col)

            # Compute both the row and column index we have not yet examined
            usedRows = set(range(0, D.shape[0])).difference(usedRows)
            usedCols = set(range(0, D.shape[1])).difference(usedCols)

            # If object centroids > no.of input centroids, check and see if some of these objects have potentially disappeared
            if D.shape[0] >= D.shape[1]:
                # Loop over the unused row indices
                for row in usedRows:
                    # Grab the object ID for the corresponding row index and increment the disappeared counter
                    objectID = objectIDs[row]
                    self.disappeared[objectID] += 1

                    # Check to see if the number of consecutive frames the object has been marked disappeared for warrants deRegistering the object
                    if self.disappeared[objectID] > self.maxDisappeared:
                        self.deRegister(objectID)

            # Otherwise, if the number of input centroids > number of existing object centroids, we need to register each new input centroid as a trackable object
            else:
                for col in usedCols:
                    self.register(inputCentroids[col])

        # Return the set of trackable objects
        return self.objects