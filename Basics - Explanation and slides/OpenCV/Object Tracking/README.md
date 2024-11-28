# Object tracking
- Most modern solutions assume the presence of a pre-trained classifier which allows us to accurately determine the object we are tracking. These classifiers are trained on tens to hundreds of thousands of images which allow us to study the patterns of the selected classes and subsequently to detect the object. 
- In case of we can't find a suitable classifier, we use 'online' or 'on the fly' training provided by 'OpenCV'.

- The tracking process is a combination of two models:
  * The motion model: tracks the speed and direction of the object's movement wich allows it to predict a new position of       the object based on the recieved data.
  * The appearnace model: determines if the object have been selected is inside the frame.
  * In case of using trained classifier, the coordinates of the bounding box containing the object would be determined           automatically, where as by using “online” training,  we specify the bounding box manually and the classifier does not       have training data, except for those that it can receive while tracking the object.
  
  # Object detection VS. Object tracking
  - Tracking is `faster` than detection: while the pre-trained classifier needs to detect an object at every frame of the video which leads to potentially high computational loads, to utilize an object tracker we specify the bounding box of an object once and based on the data on its position, speed, and direction, the tracking process goes faster.
  - Tracking is more `stable`: In cases where the tracked object is partially overlapped by another object, the detection algorithm may `LOSE` it, while the tracking algorithms are more robust to partial occlusion.
  - Tracking provides `more information`: If we are not interested in the belonging of an object to a specific class, the tracking algorithm allows us to track the movement path of a specific object, while the detection algorithm cannot.
  - Tracking allows us to apply a unique `ID` to each tracked object, making it possible for us to count unique objects in a video.
  
  # Object tracking process:
  1. Taking an initial set of object detections such as an input set of bounding box coordinates.
  2. Creating a unique ID for each of the initial detections.
  3. And then tracking each of the objects as they moves around frames in a video, maintaining the assignment of the unique IDs.
  
  # Ideal object tracking algorithm 
  1. It will only require the object detection phase once.
  2. It will be much faster than running the actual object detector itself.
  3. Be able to handle when the tracked object disappears or moves outside the boundries of the video frame (i.e., Be robust to occlusion).
  4. Be able to pick up objects it has 'LOST' in between frames.
  
  # 8 different object tracking methods using online learning classifiers(provided by OpenCV library)
  `1.` Boosting Tracker: 
  - Based on the online version of the AdaBoost algorithm - the algorithm increases the weights of incorrectly classified objects, which allows a weak classifier to “focus” on their detection.
  - Since the classifier is trained “online”, the user sets the frame in which the tracking object is located. This object is initially treated as a positive result of detection, and objects around it are treated as the background.
  - Given a new frame, the classifier is run on every pixel in the neighborhood of the previous location and the score of the classifier is recorded. The new location of the object is the one where the score is maximum.
  - As more frames come in, the classifier is updated with this additional data.
  
  #Pros | #Cons
  --- | ---
  An object is tracked quite accurately, even though the algorithm is already outdated. | Relatively low speed, strong susceptibility to noise and obstacles, and the inability to stop tracking when the object is lost.
  
  ![image](https://user-images.githubusercontent.com/91827137/183085280-5d0f1d1b-d575-4968-9bb8-c41d83cd4e37.png)

 `2.` MIL (Multiple Instance Learning) Tracker:
 - This algorithm has the same approach as BOOSTING, however, instead of guessing where the tracked object is in the next frame, an approach is used in which several potentially positive objects, called a “bag”, are selected around a positive definite object. A positive “bag” contains at least one positive result.
 
 #Pros | #Cons
 --- | ---
 More robust to noise, shows fairly good accuracy. | Relatively low speed and the impossibility of stopping tracking when the object is lost.
 
 ![image](https://user-images.githubusercontent.com/91827137/183091348-233f4dcd-1e2a-4817-ba4b-1240f8625693.png)

`3.` KCF (Kernelized Correlation Filters) Tracker:
- This tracker builds on the ideas presented in the previous two trackers. This tracker utilizes that fact that the multiple positive samples used in the MIL tracker have large overlapping regions. This overlapping data leads to some nice mathematical properties that is exploited by this tracker to make tracking faster and more accurate at the same time.

#Pros | #Cons
--- | ---
Sufficiently high speed and accuracy, stops tracking when the tracked object is lost. | Inability to continue tracking after the loss of the object.

![image](https://user-images.githubusercontent.com/91827137/183092619-5d114442-2fc9-4d07-955b-6b9522675d74.png)

`4.` TLD (Tracking Learning Detection) Tracker:
- This method allows you to decompose the task of tracking an object into three processes: tracking, learning and detecting. The tracker (based on the MedianFlow tracker) tracks the object, while the detector localizes external signs and corrects the tracker if necessary. The learning part evaluates detection errors and prevents them in the future by recognizing missed or false detections.
- The integrator combines the results of the tracking and detection modules into one bounding box.

#Pros | #Cons
--- | ---
Shows relatively good results in terms of resistance to object scaling and overlapping by other objects. | Rather unpredictable behavior, there is the instability of detection and tracking, constant loss of an object, tracking similar objects instead of the selected one.

![image](https://user-images.githubusercontent.com/91827137/183093244-2863d422-b7ac-4c7c-befa-23dc01db4c53.png)

`5.` MedianFlow Tracker:
- The algorithm tracks the movement of the object in the forward and backward directions in time and estimates the error of these trajectories, which allows the tracker to predict the further position of the object in real-time.

#Pros | #Cons
--- | ---
Excellent tracking failure reporting. Works very well when the motion is predictable and there is no occlusion. | High probability of object loss at high speed of its movement.

`6.` GOTURN (Generic Object Tracking Using Regression Network) Tracker:
- This algorithm is an “offline” tracker since it basically contains a deep convolutional neural network where Two images are fed into the network: “previous” and “current”. 
-  In the “previous” image, the position of the object is known, while in the “current” image, the position of the object must be predicted. 
- Thus, both images are passed through a convolutional neural network, the output of which is a set of 4 points representing the coordinates of the predicted bounding box containing the object. 
- Since the algorithm is based on the use of a neural network, we need to download and specify the model and weight files for further tracking of the object.

#Pros | #Cons
--- | ---
Comparatively good resistance to noise and obstructions. | The accuracy of tracking objects depends on the data on which the model was trained, which means that the algorithm may poorly track some objects selected by the user. Loses an object and shifts to another if the speed of the first one is too high.

![image](https://user-images.githubusercontent.com/91827137/183095461-06567062-3a64-49d2-b74b-30b456c798a2.png)

`7.` MOSSE (Minimum Output Sum of Squared Error) tracker:
- This algorithm is based on the calculation of `adaptive correlations` in `Fourier` space.
- The filter minimizes the sum of squared errors between the actual correlation output and the predicted correlation output. This tracker is robust to changes in lighting, scale, pose, and non-rigid deformations of the object.

#Pros | #Cons
--- | ---
Very high tracking speed, more successful in continuing tracking the object if it was lost. | High likelihood of continuing tracking if the subject is lost and does not appear in the frame.

![image](https://user-images.githubusercontent.com/91827137/183096421-74cb71fa-ae97-442f-90d9-67f21ef4ce58.png)

`8.` CSRT (Discriminative Correlation Filter with Channel and Spatial Reliability) tracker:
- This algorithm uses spatial reliability maps for adjusting the filter support to the part of the selected region from the frame for tracking, which gives an ability to increase the search area and track non-rectangular objects.
- Reliability indices reflect the quality of the studied filters by channel and are used as weights for localization.

#Pros | #Cons
--- | ---
Among the previous algorithms it shows comparatively better accuracy, resistance to overlapping by other objects. | Sufficiently low speed, an unstable operation when the object is lost.

# In colnclusion
- We can use `CSRT` when you need higher object tracking accuracy and can tolerate slower FPS throughput.
- We can use `KCF` when you need faster FPS throughput but can handle slightly lower object tracking accuracy.
- We can use `MOSSE` when you need pure speed.
