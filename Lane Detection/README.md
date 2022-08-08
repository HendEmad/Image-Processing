# Process
![lane detection](https://user-images.githubusercontent.com/91827137/183421300-f1478ce5-aad7-4c46-98ee-571b8dc95cc3.png)

# Steps
## `1.` Image preprocessing:
* Converting into Gary Scale.
* Applying Gaussian Blur to reduce the noise.
* Canny edge detector.
 
### Output

***Grayscale***

![Gray road](https://user-images.githubusercontent.com/91827137/183422193-21448ef5-7c1e-4e7a-a494-cae4f2e3c903.png)

***Gaussian Blur***

![Blured road](https://user-images.githubusercontent.com/91827137/183422257-f3bb2cba-479d-4727-b73c-60dd31b37968.png)

***Edge detector***

![Edged road](https://user-images.githubusercontent.com/91827137/183422641-c70913a2-4e25-4e4b-8a39-4ff7125fcbc5.png)

## `2.` Define ROI(Region of Interest):

### `STEPS`
* Create a black image of the same shape as that of the original image.

![image](https://user-images.githubusercontent.com/91827137/183422958-50313f76-3fd6-4b94-ba00-eb7c96cbdac8.png)

* Create a mask.

![image](https://user-images.githubusercontent.com/91827137/183423098-11502c35-71a9-464b-b030-81eb46194502.png)

* Apply the mask on our original image.

![image](https://user-images.githubusercontent.com/91827137/183423159-9e00455b-dc80-46e8-b1b7-3ba88c7838d3.png)

### final Output of ROI Funciton

![Masked road](https://user-images.githubusercontent.com/91827137/183423559-6bf4ba09-5811-441d-99d4-3b5d6ae8295e.png)


## 3. Get Lines
### Output would be
![image](https://user-images.githubusercontent.com/91827137/183423857-177e1452-67f9-40be-b9d2-23998b4c6a94.png)

## 4. Get the coordinates and set the start & end points
### Output would be
![image](https://user-images.githubusercontent.com/91827137/183424381-461baf79-9c26-418c-ae22-6404668e00dd.png)

## 5. Getting Smooth line
### Process
![image](https://user-images.githubusercontent.com/91827137/183424498-e1505916-23e5-4bcc-ab64-817cecdfa1a9.png)

### Output
![image](https://user-images.githubusercontent.com/91827137/183424907-655a2806-59d9-4b57-8dd2-6944b45ee7a6.png)

# Final Image Output
![output](https://user-images.githubusercontent.com/91827137/183425677-5b1643e0-5e48-49f6-99e2-e9dfaa8f3f49.png)
