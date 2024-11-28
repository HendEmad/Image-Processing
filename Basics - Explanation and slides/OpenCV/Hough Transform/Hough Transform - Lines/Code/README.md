# Task
Detect lines on the following image

![image](https://user-images.githubusercontent.com/91827137/183286654-fd478586-fa05-4fbf-8007-5a4c6f24127f.png)

# Steps
1. Convert images to GRAY colorspace
2. Sent the GRAY image for edge detection.
3. Call the Hough line transform funciton on the image.
4. Computing the starting and endpoint of the lines detected using the ‘rho’ and ‘theta’ values returned to us by the hough function.
5. Showing the lines on the original image using the ‘cv2.line’ function.

# Output
![image](https://user-images.githubusercontent.com/91827137/183288081-cd66834c-c46a-4043-90a2-1a016e2eec12.png)
