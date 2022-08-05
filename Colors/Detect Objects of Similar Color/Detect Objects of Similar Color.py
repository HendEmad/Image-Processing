# Step 1 – Import necessary packages and Initialize the camera
import cv2
import numpy as np

# Read the image
img = cv2.imread('img.PNG')

# define kernel size
kernel = np.ones((7, 7), np.uint8)

# Step 2 – Detect the color from the input image and create a mask
# convert to HSV colorspace
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Boundaries of green color
lower_bound = np.array([50, 20, 20])
upper_bound = np.array([100, 255, 255])

# Boundaries of Yellow color
lower_bound = np.array([20, 80, 80])
upper_bound = np.array([30, 255, 255])

# Create binary mask of the frame where the color is present.
mask = cv2.inRange(hsv, lower_bound, upper_bound)

# Step 3 – Removing unnecessary noise from masks
# Remove unnecessary black noises from the white region.
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

# Remove white noise from the black region of the mask.
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

# Step 4 – Apply the mask on the image
# Apply mask on frame in only that region where the mask is true means white.
segmented_img = cv2.bitwise_and(img, img, mask=mask)

# Step 5 – Draw a Boundary of the detected objects
# Find all the continuous points along the boundary
contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw all the contour points
output = cv2.drawContours(segmented_img, contours, -1, (0, 0, 255), 3)

# Raw boundaries in the main image.
output = cv2.drawContours(img, contours, -1, (0, 0, 255), 3)

# Showing the output
cv2.imshow("Output", output)

# Show the image
#cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()