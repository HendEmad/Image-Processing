import cv2
import numpy as np


# Convert into gray scale image
def gray(image):
    image = np.asarray(image)
    return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)


# Edge detection function
def edgeDetector(image):
    edged = cv2.Canny(image, 50, 150)
    return edged


# Region of interest function.
# we will focus on the next 100 meters to keep the car on the loan
def getROI(image):
    height, width = image.shape
    # define ROI triangle
    triangle = np.array([[(100, height), (width, height), (width - 400, int(height / 1.5))]])
    # create a black image as same as input image
    black_image = np.zeros_like(image)
    # put the triangle shape on top os the black image to create a mask
    mask = cv2.fillPoly(black_image, triangle, 255)
    # apply mask on original image
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image


# Function to detect all lines in the masked image
def getLines(image):
    lines = cv2.HoughLinesP(image, 2, np.pi/180, 100, np.array([]), minLineLength=70, maxLineGap=20)
    return lines


# Function to draw the lines on the image
def displayLines(image, lines):
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)  # Converting to 1d array
            cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 10)
    return image


# Function to get line coordinates from its parameters
def getCoordinates(image, line_parameters):
    slope = line_parameters[0]
    intercept = line_parameters[1]
    y1 = image.shape[0] # Line will always start from bottom of image
    y2 = int(y1 * (3.5 / 5))
    x1 = int((y1 - intercept) / slope)
    x2 = int((y2 - intercept) / slope)
    return np.array([x1, y1, x2, y2])


# Function to divide the lines from getLines function into left and right lines
def getSmoothLines(image, lines):
    left_fit = []  # m, c parameters for left side lines
    right_fit = []  # m, c parameters for right side lines
    for line in lines:
        x1, y1, x2, y2 = line.reshape(4)
        parameters = np.polyfit((x1, x2), (y1, y2), 1)
        slope = parameters[0]
        intercept = parameters[1]

        if slope < 0:
            left_fit.append((slope, intercept))
        else:
            right_fit.append((slope, intercept))
    # take the average of the slopes and y-intercepts from both lists
    left_fit_avg = np.average(left_fit, axis=0)
    right_fit_avg = np.average(right_fit, axis=0)

    left_line = getCoordinates(image, left_fit_avg)
    right_line = getCoordinates(image, right_fit_avg)

    return np.array([left_line, right_line])


road = cv2.imread('road.png')  # Load image

gray_road = gray(road)  # Step 1
# cv2.imwrite('Gray road.png', gray_road)  # Gray image

edged_road = edgeDetector(gray_road)  # Step 2
# cv2.imwrite("Edged road.png", edged_road)

masked_road = getROI(edged_road)  # Step 3
# cv2.imwrite("Masked road.png", masked_road)

road_lines = getLines(masked_road)  # Step 4
# cv2.imwrite("Road Lines.png", road_lines)

smooth_lines = getSmoothLines(road, road_lines)

image_with_smooth_lines = displayLines(road, smooth_lines)

cv2.imshow('Output', image_with_smooth_lines)
cv2.imwrite("output.png", image_with_smooth_lines)
cv2.waitKey(0)