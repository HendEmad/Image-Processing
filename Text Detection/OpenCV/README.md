# Introduction
A mini project to extract text from images in python using openCV and EasyOCR.

# EasyOCR 
- A deep learning-based module for reading text from all kinds of images in more than 80 languages.
- It includes image preprocessing, deep learning model recognition, and image postprocessing.
- The operations:

![image-32](https://user-images.githubusercontent.com/91827137/182976062-169c3ebb-306d-4dc0-bfac-35fd4323da2d.png)


# Steps
- First, we will install the required libraries.
- Second, we will perform image-to-text processing using EasyOCR on various images.
- Third, we will use OpenCV to overlay detected texts on the original images. Let’s get started.

# Output
### 1. EasyOCR Module output
It returns a list of detected text, with each text element containing three types of information. Which are: the text, its bounding box vertices, and the confidence level of the text detection. 
```
[([[1522, 4139], [2202, 4139], [2202, 4313], [1522, 4313]],
  'CCC 444',
  0.5483491639638102),
 ([[1636, 4300], [2011, 4300], [2011, 4351], [1636, 4351]],
  'T E $ L A . C 0 M',
  0.3179948367093998),
 ([[2519, 4358], [2635, 4358], [2635, 4388], [2519, 4388]],
  'DIAL',
  0.8864825367927551),
 ([[2644, 4362], [2790, 4362], [2790, 4388], [2644, 4388]],
  'MotoR',
  0.605705206898923)]
```

### 2. Text recognation output

![carplate](https://user-images.githubusercontent.com/91827137/182976309-31e1cbe3-15ee-47fb-99bd-1ed7d4e4af3c.png)

![digits1](https://user-images.githubusercontent.com/91827137/182976402-991b029e-154d-40ab-a2e5-256058200d8d.png)

![digits2](https://user-images.githubusercontent.com/91827137/182976428-cad6afdf-b733-441e-94b2-108a0b1007a2.png)

![hand writing](https://user-images.githubusercontent.com/91827137/182976524-c27278d9-6a20-40a6-9d56-a994ab374f7c.png)

![invoice](https://user-images.githubusercontent.com/91827137/182976603-73f076cd-e625-418d-a6c3-b527ecddbb8a.png)

![notice1](https://user-images.githubusercontent.com/91827137/182976676-2f5bffd0-813a-404f-a4c2-bf24858890ba.png)

![notice2](https://user-images.githubusercontent.com/91827137/182976860-57bc35b2-14f4-4ec3-a765-47d14595ea16.png)

# Resources
https://github.com/JaidedAI/EasyOCR

https://pytorch.org/get-started/locally/
