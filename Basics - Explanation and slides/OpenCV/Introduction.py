import cv2
import numpy as np

# Kernel
kernel = np.ones((5, 5), np.int8)

# Image: One frame
# Load image
img = cv2.imread("resources/1.jpg")

# Show image
cv2.imshow("Image", img)

# Add a delay
cv2.waitKey(0)

# Video: more than one frame --> loop
frameWidth = 640
frameHeight = 360
# Import video(mp4)
cap = cv2.VideoCapture("resources/video1.mp4")
# Read each frame
while True:
    # It reads frames from `cap`, then stores them in `img` If we want to sure that the frame is grabbed,
    # we can check the value of `success`. If true, the frame is grabbed successfully.
    success, img = cap.read()
    # To resize the video
    img = cv2.resize(img, (frameWidth, frameHeight))
    # Show each frame as video
    cv2.imshow("Video", img)
    # Add a delay
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Webcam: more than one frame --> loop
frameWidth = 640
frameHeight = 360

# Import video(Webcam)
cap = cv2.VideoCapture(0)
# set width and height of webcam device to the default values of opencv
cap.set(3, frameWidth)
cap.set(4, frameHeight)
# Read each frame
while True:
    # It reads frames from `cap`, then stores them in `img` If we want to sure that the frame is grabbed,
    # we can check the value of `success`. If true, the frame is grabbed successfully.
    success, img = cap.read()
    # Show each frame as video
    cv2.imshow("Video", img)
    # Add a delay
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# greyscale
path = "resources/lenna.jpeg"
# import the image
img = cv2.imread(path, 0)
# display the image
cv2.imshow("Lenna", img)
cv2.waitKey(0)

# greyscale --> 2nd method
path = "resources/lenna.jpeg"
img = cv2.imread(path)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Lenna", img)
cv2.imshow("Lenna Gray", imgGray)
cv2.waitKey(0)

# Blurring
path = "resources/lenna.jpeg"
img = cv2.imread(path)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 0)
imgBlur2 = cv2.GaussianBlur(imgGray, (9, 9), 0)
cv2.imshow("Lenna", img)
cv2.imshow("Lenna Gray", imgGray)
cv2.imshow("Lenna Blur", imgBlur)
cv2.imshow("Lenna Blur2", imgBlur2)
cv2.waitKey(0)

# Edge detector
path = "resources/lenna.jpeg"
img = cv2.imread(path)
imgCanny = cv2.Canny(img, 100, 100)
imgCanny2 = cv2.Canny(img, 200, 200)
imgCanny3 = cv2.Canny(img, 20, 20)
cv2.imshow("lenna", img)
cv2.imshow("Lenna Canny", imgCanny)
cv2.imshow("Lenna Canny 2", imgCanny2)
cv2.imshow("Lenna Canny 3", imgCanny3)
cv2.waitKey(0)

# Morphological operations (Dilation & Erosion): Increase and decrease the size of images(the actual thickness of the
# lines that is around the boundaries of the image)
path = "resources/lenna.jpeg"
img = cv2.imread(path)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
imgCanny = cv2.Canny(img, 100, 200)
# dilation
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
# Erosion
imgErosion = cv2.erode(imgDilation, kernel, iterations=2)
cv2.imshow("Lenna", img)
cv2.imshow("Lenna_Gray", imgGray)
cv2.imshow("Lenna_Blur", imgBlur)
cv2.imshow("Lenna_Canny", imgCanny)
cv2.imshow("lenna_Dilation", imgDilation)
cv2.imshow("Lenna_Erosion", imgErosion)
cv2.waitKey(0)

# Resize images
path = "resources/road.jpg"
img = cv2.imread(path)
# Display the size of the image(height, width, 3channels (B-G-R))
print(img.shape)
# To resize the image
width, height = 400, 400
imgResized = cv2.resize(img, (width, height))
print(imgResized.shape)
cv2.imshow("Road", img)
cv2.imshow("Road_Resized", imgResized)
cv2.waitKey(0)

# Crop images
path = "resources/road.jpg"
img = cv2.imread(path)
# Cropping
imgCropped = img[412:882, 0:1250]
# cv2.imshow("Road", img)
cv2.imshow("Road_Cropped", imgCropped)
cv2.waitKey(0)

# Create BLANK image
# One channel image(black / white)
img = np.zeros((512, 512))
# Add color functionality
img_color = np.zeros((512, 512, 3), np.uint8)  # Unsigned int 0:255
# Display the size of the image
print(img.shape)
print(img_color.shape)
# Display the matrix of the image
print("Size of float values' image: \n", img)
print("Size of int values' image: \n", img_color)
cv2.imshow("Blank image", img)
cv2.imshow("Colored image", img_color)
cv2.waitKey(0)

# Create COLORD image
img_1 = np.zeros((512, 512, 3), np.uint8)
img_2 = np.zeros((512, 512, 3), np.uint8)
# If color = Blue ---> BGR = 255, 0, 0(Blue Green Red), AND so on
img_1[:] = 255, 0, 0
img_1[250:512] = 0, 0, 255
img_2[:250] = 0, 255, 0
cv2.imshow("Blue image", img_1)
cv2.imshow("Green image", img_2)
cv2.waitKey(0)

# Create shapes
img = np.zeros((512, 512, 3), np.uint8)
# create line ---> .line(image, point1, point2, color, thickness)
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 255), 2)
# create rectangle
cv2.rectangle(img, (350, 100), (450, 200), (255, 255, 0), 2)
cv2.rectangle(img, (10, 300), (100, 500), (255, 0, 255), cv2.FILLED)
# Create circle --> .circle(image, center point, radius, color, thickness)
cv2.circle(img, (200, 400), 50, (255, 0, 0), 3)
cv2.circle(img, (200, 400), 25, (255, 0, 0), cv2.FILLED)
# Write text ---> .putText(image, text, starting position, font type, font scale, color, thickness)
cv2.putText(img, "Drawing shapes", (110, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 1)
cv2.imshow("Image", img)
cv2.waitKey(0)

# Images stacking(joining multiple images together), this way requires many lines of code in case having many images
# --> this way is not efficient. It can be done using matplotlib, but it is very slow in videos ar webcam stream.
img1 = cv2.imread("resources/lenna.jpeg", 0)
img2 = cv2.imread("resources/road.jpg")
# Images scaling; to make sure that the joined image will not be out of screen.
# Horizontally & vertically stacking MUST get same-size images
img1 = cv2.resize(img1, (350, 350), None, 0.5, 0.5)
img2 = cv2.resize(img2, (350, 350), None, 0.5, 0.5)
# Converting the grayscale img1 into BGR image
img1 = cv2.cvtColor(img1, cv2.COLOR_GRAY2BGR)
# Stacking images' arrays horizontally
hor = np.hstack((img1, img2))
# Stacking images' arrays horizontally
ver = np.vstack((img1, img2))
# displaying the results
cv2.imshow("Vertical stacking", ver)
cv2.imshow("Horizontal stacking", hor)
cv2.waitKey(0)

# Warp Perspective / Bird View [6]
img = cv2.imread("resources/cards.jpg")

width, height = 250, 350
pts1 = np.float32([[111, 219], [287, 188], [154, 482], [352, 440]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

for x in range(0, 4):
    cv2.circle(img, (pts1[x][0], pts1[x][1]), 5, (0, 0, 255), cv2.FILLED)
cv2.imshow("Original image", img)
cv2.imshow("Output image", imgOutput)

cv2.waitKey(0)