# Description
- This program was created using Python and the OpenCV library.
- It takes in an image of random shapes and is able to detect the name of that shape, the area and the perimeter.

# Code requirements (With versions I tested on):
- Python (3.10.5)
- OpenCV (4.6.0)
- Numpy (1.23.1)

# Code:
The code does the following:
- Reading the image and converting from RGB to Gray scale.
- Removing Gaussian Noise via Gaussian Blur.
- Finding all Countours in the processed image
- Filtering countours based on their area.
- Initializing a new image and drawing the filtered contours.

# Results:
### Input:
<img width="740" alt="shapes (1)" src="https://user-images.githubusercontent.com/91827137/179821950-3754a2ec-81f2-481d-ac41-dc8dce9cc0db.png">

### Output:
<img width="495" alt="output" src="https://user-images.githubusercontent.com/91827137/179824482-cd76b07b-75fb-462e-b307-b8c2e1a71af8.png">
