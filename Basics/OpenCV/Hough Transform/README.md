# Hough Transform
Computer Vision technique used for the purpose of feature isolation of particular shapes in images and videos (as straight lines).

## Hough space
We can represent a straight line as: `y = mx + b`, It can alsp be represented as: `ρ = x*cos(θ) + y*sin(θ)` in polar coordinate where:
   * ρ is the distance from the origin.
   * θ is the angle formed by perendecular line and horizontal                                         axis measured in the counter-clockwise direction.
   
We represented the line in two values (ρ, θ) which can be plotted in a space known as `Hough space`.

![photo](https://user-images.githubusercontent.com/91827137/183283455-e49ee3c3-97a9-4b8c-bfe4-58cf34361769.PNG)

## Why don't we use the `y = mx + c` form?
In polar form , the slope(m) can take values from –∞ to +∞. For the Hough transform, the parameters need to be bounded.

***We can imagine that θ is bounded but it seems that ρ takes values from 0 to +∞!***

It may be true in theory, but in practice, ρ is also bounded beacause the `image itself is finite`.

## To get maximum performance
Pass the image to the edge detector first before applying Hough transform.

# Hough Transform implementation in OpenCV
`lines = cv2.HoughLines(image, ρ, θ, threshold)`

- where: 
  * image: Image src.
  * ρ: Distance resolution of the accumulator(distance from the coordinate origin in the hough space).
   * θ: Angle resolution of the accumulator(line rotation in radians)
   * threshold: Accumulator threshold parameter(Lines are only selected if they get votes = threshold value).
- This funciton returns an (2Darray) of sub-arrays containing 2 elements, each representing ρ and θ for the line detected.

# How do we get this equation `ρ = x*cos(θ) + y*sin(θ)` from `y = mx + b`?
from basic trigonometry:

sin θ = opposite / hypotenuse && cos θ = adjacent / hypotenuse

m = slope of ρ (line) = -tan(90-θ) = -cos(θ) / sin(θ)

b = ρ / sin(θ)

so y = (-cos(θ)/sin(θ)) * x + (ρ / sin(θ)) -->   y*sin(θ) = -cos(θ) * x + ρ

so: ρ = x cos(θ) + y sin(θ)

![image](https://user-images.githubusercontent.com/91827137/183288883-e5fdb4d4-d9c2-40be-9df8-c581004edc87.png)
