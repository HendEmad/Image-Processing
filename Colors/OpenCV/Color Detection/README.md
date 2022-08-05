# Color Detection
- A mini project to automatically get the name of the color by clicking on them.

- The dataset contains the color name and its values, we will calculate the distance from each color and find the shortest one.

# Dataset
- Colors are made up of 3 primary colors (Red, Green, and Blue). In computers, we define each color value within a range of 0 to 255. So, we can define a color in 256*256*256 = 16,581,375 which are approximately 16.5 million different ways to represent a color. In our dataset, we need to map each color’s values with their corresponding names. We will be using a dataset that contains RGB values with their corresponding names.
- The colors.csv file includes 865 color names along with their RGB and hex values.

# Packages used:
- `Numpy`
- `Pandas`
- `OpenCV`

# Steps
- Taking an image from the user and reading the CSV file with pandas.
- Set a mouse callback event on a window.
- Create the draw_function.
- Calculate distance to get color name.
- Display image on the window.
