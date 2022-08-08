This project aims to process an image and find obstacles(in specific color) and the minimum path between two similar objects using OpenCV.

Finding the shortest path between a source and destination is called `Path Planning`.

# Input
A set of test images, each containing:
- 10x10 grid, making 100 squares.
- Obstacles marked as black square.
- Objects defined by three features: Shape, Size and Color.

![img](https://user-images.githubusercontent.com/91827137/183492192-9f911626-50d7-46b4-962f-2dcac73c527e.png)
![img_1](https://user-images.githubusercontent.com/91827137/183492304-eecd8301-12d4-40cd-8a1d-94bc6474490e.png)
![img_2](https://user-images.githubusercontent.com/91827137/183492316-9dc91be2-6b48-4217-af82-347161bb57cd.png)
![img_3](https://user-images.githubusercontent.com/91827137/183492353-45abc65e-621b-4113-a167-7bea172df6f8.png)

- The squares are identified by the coordinates (x, y) where x is the column, and y is the row.
- Each square can be empty or have an Obstacle or have an Object.

# Files description
- `test.py` --> to check the results. You can edit the test image from main.py to see different results.
- `obstacles_detection.py` --> To see the main functionality and run it. 
- `astarsearch.py` --> The implementation of A* search algo.
- `traversal.py` --> To traverse through the image to find objects/min path.

# Output example
![image](https://user-images.githubusercontent.com/91827137/183494879-32e1f438-14fc-4dc8-9a99-c4ada329301f.png)

# More explanation
1. The coordinates of occupied grid: 
- returns a list having tuples of deontes number.
-  Grid is to be considered occupied if either grid has an Obstacle or an Object.
------------------------------------------------------------------------------------
2. The minimum path:
- A* search is used to find this shortest path.
- For each object in the test images, a matching object which is nearest to it is found using structural_similarity function from scikit-image.
- Object is said to be nearest to another Object, if length of path traversed between two objects is smallest.
- Traversal is done by moving either horizontally or vertically.
- The length of the path is determined by the number of moves made during traversal.
- The code return a python dictionary:
  * Key for dictionary is a tuple - (x,y) coordinate of an Object
  * First element of dictionary is a tuple - (x,y) coordinate of an object nearest to it
  * Second element is a list of tuples having (x,y) coordinate of all grids traversed i.e all route path
  * Third element of dictionary should be number of moves taken for traversal.
