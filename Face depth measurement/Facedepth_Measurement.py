# Import libraries
import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector

# Steps:
'''
1. detect the face using this line: `detector = FaceMeshDetector(maxFaces=1)`
2. find the mesh(points of the face = 468) and return it to the face detected using this line: `img, faces = detector.findFaceMesh(img, draw=False)`
3. find the points of our eyes and draw them:
```
pointLeft = face[145]
pointRight = face[374]
cv2.circle(img, pointLeft, 5, (255, 0, 255), cv2.FILLED)
cv2.circle(img, pointRight, 5, (255, 0, 255), cv2.FILLED)
```
4. Draw the line between eyes points which will represent the distance between them
'This line distance will be constant in reality, but in pixels it will be different based on the distance between the camera and the face,
Based on this difference in pixels, the distance from the camera to the face can be calculated: `cv2.line(img, pointLeft, pointRight, (0, 200, 0), 3)`
5. Calculate the focal length by making the W is constant which represents the width of eyes in reality [62 mm in women and 64 mm in men, average is 63 mm]
and a constant d (making the distance between your face and the camera is constant) and w is the distance between eyes in pixels
'''

# Create the webCam object
cap = cv2.VideoCapture(1)
# To find the face
detector = FaceMeshDetector(maxFaces=1)

while True:
    success, img = cap.read()
    img, faces = detector.findFaceMesh(img, draw=False)  # 468 points for one face

    if faces:  # If any face is available
        face = faces[0]  # Take the first face as maxFaces we inputted is 1(maxFaces=1), this will always be true
        # Detect the landmark, so we need to tell which points we need.
        # We will need point of the left, and point of the right
        pointLeft = face[145]  # Those points pointLeft&pointRight for eyes detection
        pointRight = face[374]  # pointLeft and pointRight points are found by testing

        # # Drawing #
        # # Draw a line between the eyes points
        # cv2.line(img, pointLeft, pointRight, (0, 200, 0), 3)  # image, startpoint, endpoint, color, thickness
        # cv2.circle(img, pointLeft, 5, (255, 0, 255), cv2.FILLED)  # image, center position, radius, color
        # cv2.circle(img, pointRight, 5, (255, 0, 255), cv2.FILLED)

        w,_ = detector.findDistance(pointLeft, pointRight)  # _ is used to ignore the values regardless of the distance
        W = 6.3  # in cm; constant

        # # Finding the focal length , we will not need it after calculating the focal length#
        # # Find the distance between eyes in pixels(w)
        # d = 50  # random
        # f = (w * d) / W  # Focal point
        # print(f)  # Almost 1415

        # Finding distance #
        f = 1415
        d = (W * f) / w
        print(d)

        # Put the distance on the image of the face
        cvzone.putTextRect(img, f'Depth is: {int(d)} cm',
                           (face[10][0]-100, face[10][1]-50),
                           scale=1.8)  # image, text to write, position to write,

    cv2.imshow("Image", img)
    cv2.waitKey(1)  # 1ms delay
