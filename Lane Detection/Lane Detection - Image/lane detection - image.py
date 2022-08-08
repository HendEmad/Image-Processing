# IMPORT LIBRARIES
import cv2
import numpy as np


# Convert into gray scale image
def gray(image):
    image = np.asarray(image)
    return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)


# Gaussian blur to reduce noise and smoothen the image
def gauss(image):
    return cv2.GaussianBlur(image, (5, 5), 0)


# Edge detection function
def edgeDetector(image):
    edged = cv2.Canny(image, 50, 150)
    return edged


# Function to isolate the edges that correspond with the lane lines
# we will focus on the next 100 meters to keep the car on the loan
def getROI(image):
    # extract image dimensions
    height, width = image.shape
    # define the triangle (which represents the region to be isolated) dimensions
    triangle = np.array([[(100, height), (width, height), (width - 400, int(height / 1.5))]])
    # create a black plane to define a white triangle with the same dimensions
    black_image = np.zeros_like(image)
    # create a mask (triangle that isolates the region of interest in our image)
    mask = cv2.fillPoly(black_image, triangle, 255)
    # isolate the edges that correspond with the lane lines
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image


# Function to detect all lines in the masked image
# Applying Hough line transform to convert the clusters of white pixels from the isolated region into actual lines
# The output is all lines detected in the image, each line segment has 2 coordinates
# One denote the start of the line, and the other marks the end of the line
def getLines(image):
    lines = cv2.HoughLinesP(image, 2, np.pi / 180, 100, np.array([]), minLineLength=70, maxLineGap=20)
    print(lines)
    return lines


# Function to draw the lines on the image
def displayLines(image, lines):
    # make sure that the lists with the line points is not empty
    if lines is not None:
        # loop through the lists
        for line in lines:
            # extract the two pairs of(x, y) coordinates
            x1, y1, x2, y2 = line.reshape(4)  # Converting to 1d array
            # create the line and paste it onto the black image
            cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 10)
            print(x1, " ", y1, " ", x2, " ", y2)
    return image


# Function to get line coordinates from its parameters
def make_points(image, line_parameters):
    slope = line_parameters[0]
    intercept = line_parameters[1]
    # define the height of the lines,
    # In OpenCV, the y-axis in inverted, so the 0 is at the top and height is at origin
    y1 = image.shape[0]  # Line will always start from bottom of image
    # we want the line to start at the origin (y1) and end ar 2/5 up the image
    # since the y-axis is inverted, instead of 3/5 up from 0, we see 2/5 from the max height
    y2 = int(y1 * (3.5 / 5))
    # calculate x coordinates from the equation: y = mx + b
    # x = (y - b0 / m)
    x1 = int((y1 - intercept) / slope)
    x2 = int((y2 - intercept) / slope)
    print(y1, " ", y2, " ", x1, " ", x2)
    # return the sets of coordinates
    return np.array([x1, y1, x2, y2])


# Function to divide the lines from getLines function into left and right lines
def getSmoothLines(image, lines):
    left_fit = []  # m, c parameters for left side lines
    right_fit = []  # m, c parameters for right side lines
    # loop through the array of lines
    for line in lines:
        # extract the (x, y) values of the 2 points from each line segment
        x1, y1, x2, y2 = line.reshape(4)
        # fit line to point, return slope and y-int
        parameters = np.polyfit((x1, x2), (y1, y2), 1)
        # determine the slope and y-intercept of each line segment
        slope = parameters[0]
        intercept = parameters[1]
        # add negative slopes to the list of left lines and the positive slopes to the list with the right lines
        if slope < 0:
            left_fit.append((slope, intercept))
        else:
            right_fit.append((slope, intercept))

    # Take the avg of the slopes and y-intercepts from both lists
    # take the avg of all line segments for both lists
    left_fit_avg = np.average(left_fit, axis=0)
    right_fit_avg = np.average(right_fit, axis=0)
    # calculate the start point and endpoint for each line
    left_line = make_points(image, left_fit_avg)
    right_line = make_points(image, right_fit_avg)
    # return 2 coordinated for each line
    return np.array([left_line, right_line])


road = cv2.imread('road.png')  # Load image

gray_road = gray(road)  # Step 1
cv2.imwrite('Gray road.png', gray_road)  # Gray image

blur_road = gauss(gray_road)
cv2.imwrite('Blured road.png', blur_road)

edged_road = edgeDetector(blur_road)  # Step 2
cv2.imwrite("Edged road.png", edged_road)

masked_road = getROI(edged_road)  # Step 3
cv2.imwrite("Masked road.png", masked_road)

road_lines = getLines(masked_road)  # Step 4
cv2.imwrite("Road Lines.png", road_lines)

smooth_lines = getSmoothLines(road, road_lines)

image_with_smooth_lines = displayLines(road, smooth_lines)

cv2.imshow('Output', image_with_smooth_lines)
cv2.imwrite("output.png", image_with_smooth_lines)
cv2.waitKey(0)
