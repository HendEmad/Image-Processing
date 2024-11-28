The equation of circle can be represented using three parameters: (x, y, raduis) where (x, y) is the center of the circle.

![image](https://user-images.githubusercontent.com/91827137/183290261-8f400f9e-df4a-4366-a080-6e35d569fce9.png)

# Circles detection using Hough transform
`circles = cv2.HoughCircles(img_blur, cv2.HOUGH_GRADIENT, dp, mindst, param1, param2, minRadius, maxRadius)`

- Where:
  * image: The input image.
  * method: Detection method.
  * dp: the Inverse ratio of accumulator resolution and image resolution.
  * mindst: minimum distance between centers od detected circles.
  * param_1 and param_2: These are method specific parameters.
  * min_Radius: minimum radius of the circle to be detected.
  * max_Radius: maximum radius to be detected.
- This function returns a 3d array of x, y and r
- `HoughCircles` function has inbuilt canny detection, therefore it is not required to detect edges explicitly in it.
