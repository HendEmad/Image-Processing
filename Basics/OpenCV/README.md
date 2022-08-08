# Image preprocessing

### 1. GreyScale
- Complexity of grey level images in lower than that of color images.
- Function: `cv2.cvtColor`

### 2. Gaussian Filter
- To reduce noise in the image. It is needed in Canny-edge detector as the gradients of Canny are very sensitive to noise.
- Funciton: `cv2.GaussianBlur(img, ksize, sigma)`, its parameters:
  * img:Image
  * ksize:dimension of the kerenel which we convolute over the image.
  * sigma: defines the standard deviation along x axis.
  
### 3. canny-edge detection
- To detect sharp changes.
- Function: `cv2.Canny(img, threshold1, threshold2)`, its parameters:
  * img: image.
  * threshold1: filters all gradients lower than this number (they aren’t considered as edges).
  * threshold2: determines the value for which an edge should be considered valid.
  * Any gradient in between the two thresholds will be considered if it is attached to another gradient whi is above threshold2.
