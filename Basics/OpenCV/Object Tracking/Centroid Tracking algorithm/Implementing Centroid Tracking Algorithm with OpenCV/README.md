[Algorithm's Logic & steps](https://github.com/HendEmad/Image-Processing-projects/tree/main/Basics/OpenCV/Object%20Tracking/Centroid%20Tracking%20algorithm)

# Code Explanation
```
class CentroidTracker:
    def __init__(self, maxDisappeared=50):
        # Initialize the next unique object ID along with two ordered dictionaries used to keep track of mapping a given object ID to its centroid and number
        # of consecutive frames it has been marked as disappeared, respectively
        self.nextObjectID = 0
        self.objects = OrderedDict()
        self.disappeared = OrderedDict()

        # Store the number of maximum consecutive frames a given object is allowed to be marked as disappeared until we need to deRegister the object from tracking
        self.maxDisappeared = maxDisappeared
```
Here we defined the `CentroidTracker` class where it accepts a single parameter, the maximum number of consecutive frames a given object has to be lost/disappeared till we remove it from out tracker.

The constructor builds four class variables:
- `nextObjectID`: A counter used to assign unique IDs to each object. 
    * In the case that an object leaves the frame and does not come back for `maxDisappeared` frames, a new(next) object ID would be assigned.
- `objects`: A dictionary that utilizes the object ID as the key and the centroid (x, y)-coordinates as the value.
- `disappeared`: Maintains number of consecutive frames (value) a particular object ID (key) has been marked as “lost”for
- `maxDisappeared`: The number of consecutive frames an object is allowed to be marked as “lost/disappeared” until we deregister the object.

----------------------------------

```
# Method responsible for adding new objects to our tracker
    def register(self, centroid):
        # When registering an object, we use the next available object ID to store the centroid
        self.objects[self.nextObjectID] = centroid
        self.disappeared[self.nextObjectID] = 0
        self.nextObjectID += 1
```

- This function accepts a `centroid` and then adds it to the `objects` dictionary using the next available object ID;

- The number of times an object has disappeared is initialized to `0` in the `disappeared` dictionary .

- Finally, we increment the nextObjectID so that if a new object comes into view, it will be associated with a unique ID.

----------------------------------------

```
# Method for removing objects from out tracker
    def deRegister(self, objectID):
        # To deRegister an object ID, we delete the object ID from both of our respective dictionaries
        del self.objects[objectID]
        del self.disappeared[objectID]
```

 we also need the ability to remove old ones that have been lost or disappeared from our the input frames themselves.
 
 It simply deletes the `objectID` in both the `objects` and `disappeared` dictionaries, respectively.
