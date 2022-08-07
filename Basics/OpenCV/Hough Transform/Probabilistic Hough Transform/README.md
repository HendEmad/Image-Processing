It is an optimized version of Hough Transform because:
- The lines that are predicted here are not unbounded (infinite).
- They are enclosed in an area where the probability is maximum.

# Probabilistic Hough Transform OpenCV Function
`lines = cv2.HoughLinesP(image,rho,theta,threshold,minLineLength,maxLineGap)`

- Returns 4 values for each sub-array, namely the start and endpoints.
- Where:
  * image: Image src rho: Distance resolution of the accumulator (distance from the coordinate origin in the hough space).
  * theta: Angle resolution of the accumulator(Line rotation in radians).
  * threshold: Accumulator threshold parameter(Lines are only selected if they get votes equal to the threshold value)).
  * minLineLength: Line segments shorter than this value are rejected.
  * maxLineGap: Max allowd gap between line segments to treat them as a single line.


