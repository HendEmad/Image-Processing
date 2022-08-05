# Color Detection
- A mini project to automatically get the name of the color by clicking on them.

- The dataset contains the color name and its values, we will calculate the distance from each color and find the shortest one.

# Dataset
- Colors are made up of 3 primary colors (Red, Green, and Blue). In computers, we define each color value within a range of 0 to 255. So, we can define a color in 256*256*256 = 16,581,375 which are approximately 16.5 million different ways to represent a color. In our dataset, we need to map each color’s values with their corresponding names. We will be using a dataset that contains RGB values with their corresponding names.
- The colors.csv file includes 865 color names along with their RGB and hex values.

# Packages used:
- `Pandas`
- `OpenCV`

# Steps
- Reading inout image and the CSV file with pandas.
- Set a mouse callback event on a window.
- Create the draw_function.
- Calculate distance to get color name.
- Display image on the window.

# Output
![output1](https://user-images.githubusercontent.com/91827137/183000319-53118502-6238-4e3e-9305-8ff2e3e63bf8.PNG)

![output2](https://user-images.githubusercontent.com/91827137/183000363-78102e64-ca4c-483b-8b48-f98a92099ada.PNG)

![Output3](https://user-images.githubusercontent.com/91827137/183000405-b8b99f92-d40e-4960-9ab5-ba38b5085a0c.PNG)

![output4](https://user-images.githubusercontent.com/91827137/183000455-c2e8fa1e-8a55-4f0c-874b-70bbf2523754.PNG)
