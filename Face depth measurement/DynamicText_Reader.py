# Import libraries
import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
import numpy as np

# STEPS
'''
1. calculate the distance between the face and the camera (Steps in FaceDepth_Measurement)
2. Create an empty window, and inside it, write some text:
   2.1. Create an image of zeros with the same size of the original image using numpy: `imgText = np.zeros_like(img)`
   2.2. Stack the two images together: `imgStacked = cvzone.stackImages([img, imgText], 2, 1)`
   2.3. Write the text to want to appear in the second image:
   ```
   textList = ["Welcome...", "Here, we are......", "Here we calculate the distance",
            "between the camera and the detected face", "and applying them to application",
            "to decrease and increase the text size depending on this calculated distance."]
   ```
   2.4. We can make the text appearing during detecting the face, otherwise, it will not appear
        2.4.1. Write the text on the imgText:
        ```
            for i, text in enumerate(textList):  
                singleHeight = 50
                # Write the test
                cv2.putText(imgText, text, [50, 50+(i*singleHeight)],
                cv2.FONT_ITALIC, 1, (255, 255, 255), 2)
        ```
        2.4.2. Add dynamic to scale and make it more stable using some calculations in `int((int(d/10)*10)/4)`
        and in `(int(d/10)*10)/75`  
        ```
        singleHeight = 20 + int((int(d/10)*10)/4)
        scale = 0.4 + (int(d/10)*10)/75  
        # Write the test
        cv2.putText(imgText, text, [50, 50+(i*singleHeight)],
                    cv2.FONT_ITALIC, scale, (255, 255, 255), 2)
        ```
'''


cap = cv2.VideoCapture(1)
detector = FaceMeshDetector(maxFaces=1)

# Add the text, multiple lines ==> list not just string
textList = ["Welcome...", "Here, we are......", "Here we calculate the distance",
            "between the camera and ", "the detected face", "and applying them to application",
            "to decrease and increase another text", "size depending on this calculated", "distance."]


while True:
    success, img = cap.read()
    # Create another image with the same size but its pixels values are zeros (black image)
    imgText = np.zeros_like(img)
    img, faces = detector.findFaceMesh(img, draw=False)

    if faces:
        face = faces[0]
        # Detect the landmark
        pointLeft = face[145]
        pointRight = face[374]

        w, _ = detector.findDistance(pointLeft, pointRight)  # _ is used to ignore the values regardless of the distance
        W = 6.3  # in cm

        # Finding distance #
        f = 1415
        d = (W * f) / w
        print(d)

        # Put the distance on the image of the face
        cvzone.putTextRect(img, f'Depth is: {int(d)} cm',
                           (face[10][0]-100, face[10][1]-50),
                           scale=1.8)
        sensitivity = 10  # More value is less sensitivity
        for i, text in enumerate(textList):  # i ==> for iteration number of enumerate()
            singleHeight = 20 + int((int(d/sensitivity)*sensitivity)/4)
            scale = 0.2 + (int(d/sensitivity)*sensitivity)/75  # 0.4 minimum; add a certain value to it
            # Write the test
            cv2.putText(imgText, text, [50, 50+(i*singleHeight)],
                        cv2.FONT_ITALIC, scale, (255, 255, 255), 2)
            # image, text to write, origin[width, dynamic height(height + height of every single line)], font, scale, color, thickness

    imgStacked = cvzone.stackImages([img, imgText], 2, 1)  # [two images], columns, scale
    cv2.imshow("Image", imgStacked)
    cv2.waitKey(1)  # 1ms delay
