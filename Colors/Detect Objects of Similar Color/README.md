# Detect Objects of Similar Color
A mini project for basic object detection by color using two image processing techniques:
- `Color detection`
- `Image segmentation`

### 1. Color detection:
A technique of detecting any color in a given range of HSV (hue saturation value) color space.

### 2. Image segmentation:
The process of partitioning digital image and labeling every pixel, where each pixel having the same label shares certain characteristics.

# Packages
- `Numpy`
- `OpenCV`

# Steps
- Import necessary packages and read the image.
- Detect the color from the input image and create a mask.
- Removing unnecessary noise from masks.
- Apply the mask to the image.
- Draw a Boundary of the detected objects.

# HSV ColorApace
A cylindrical colorspace stands for HUE, SATURATION, and VALUE (brightness):
- HUE: An angular dimension that encodes color information.
- SATURATION: Encodes the intensity of color.
- VALUE: Represents the amount to which that respective color is mixed with black.

# OUtput
![yellow output](https://user-images.githubusercontent.com/91827137/183004735-a925cd0c-d144-4c8f-8c60-b3602a8014f6.PNG)

![green output](https://user-images.githubusercontent.com/91827137/183004749-30a4f985-5253-4db6-b067-dc50f5c1fc3e.PNG)
