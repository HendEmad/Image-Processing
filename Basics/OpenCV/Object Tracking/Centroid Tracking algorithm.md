# Centroid based Object Tracking

### Logic
- It utilizes the Euclidean distance between the centroids of the objects detected between two consecutive frames in a video.
- Then, it compares the Euclidean distance with a threshold value:
    * if Euclidean distance < threshold, then the same object in motion;
    * else, assign new object ID;
    * if an eisting object no longer exists, then the tracking for that object is removed;

### Steps
--note that each frame may contain more than one object, which means that we assign a unique ID for each object for each frame, and also we compute the centroid for each bound box for each object in each frame.

`Step 1`: Object/s are detected using a bounding box for the frame at time ***t-1***.

`Step 2`: Calculate the centroids for the object/s detected for the frame at time ***t-1***.

`Step 3`: Assign a unique ID for the frame at ***t-1***.

![photo1](https://user-images.githubusercontent.com/91827137/183262914-8ef2bd42-40ce-4ae1-8199-3488dc7b2516.png)

`Step 4`: Objects are detected using a bounding box for the frame at time ***t*** (objects of the second frame).

`Step 5`: Instead of assigning a new ID each detectd object, we first need to compute Euclidean distance between new bounding boxes(centroids of all objects detected in frame t) and the existing bounding boxed(centroids of all objects detected in frame t-1)

![photot 2](https://user-images.githubusercontent.com/91827137/183265813-55f1fa82-83a7-4620-b5e4-b9f683d948ee.PNG)

In figure 2, we have detected three objects in oui image frame. The two pairs that are clode together are two existing objects.

`Step 6`: The primary assumption of the centroid tracking algorithm is that a given objext will potentially move between subsequent frame, but the distance between the centroids for frames ![image](https://user-images.githubusercontent.com/91827137/183265878-2616ae36-a449-4733-a6bf-61e0475b1fbb.png) and  ![image](https://user-images.githubusercontent.com/91827137/183265884-48dabc65-3ffa-439f-a9b7-456f3e67203a.png) will be smaller than all other distances between objects, Therefore, if we choose to associate centroids with minimum distances between subsequent frames we can build our object tracker.

![image](https://user-images.githubusercontent.com/91827137/183266305-5084e69b-a274-4c17-a472-dfd6879a0e7e.png)

In Figure 3, we can see how our centroid tracker algorithm chooses to associate centroids that minimize their respective Euclidean distances.

### What about the lonely point in the bottom-left? It didn't get associated with anything..Whar do we do with it?

The answer is `Step 7` which is register new objects:

- We need ti register new object in the event that there are more input detections than existing objects being tracked.
- Registering simply means that we are adding the new object to our list of tracked objects by:
  * Assiging it a new object ID.
  * Storing the centroid of the bounding box coordinates for that object.
  * Then compute the Euclidean distance between new bounding boxes and existing objects (repeat starting from step `5`), and repeat the pipeline of the steps again strarting from this step.

![photo1](https://user-images.githubusercontent.com/91827137/183266592-95a5ee02-02d2-44a1-81b9-1a7ae2ff9da2.png)

What if the object has been lost, disappeared, or left the field of view ... How can we handle this?

The answer of this question leads to `Step 8`.

`Step 8`: Deregister old objects:

One way we can handle this situation through is deregistering old objects when they cannot be matched to any existing objects for a total of N subsequent frames.
