DataSet Source: https://sid.erda.dk/public/archives/daaeac0d7ce1152aea9b61d9f1e19370/published-archive.html

# Description
This project is a traffic signs detection and classification system on videos using OpenCV. The detection phase uses Image Processing techniques that create contours on each video frame and find all ellipses or circles among those contours. They are marked as candidates for traffic signs.

# Problem Definition:
`Type` Image Classification

`Method` Convolution Neural Network(CNN)

`Tasks`

1. Explore the dataset.
2. Build a CNN model.
3. Train and validate the model.
4. Test the model with test dataset.

## DataSet Summary
Once loaded, the training, validation, and test data are stored in numpy arrays. Using the shape property of numpy arrays I get the following summary statistics of the traffic signs data set:
- The size of training set is: 22271
- The size of the validation set is: 5568
- The size of test set is: 6960
- The shape of a traffic sign image is: (32, 32, 3)
- The number of unique classes/labels in the data set is 43

## Exploratory Visualization
It is interesting to observe how the classes are not homogeneously distributed among the training data. Validation and Testing data present a similar distribution. This can relevant for the accuracy of classes that appear less frequently on the training data.

![image](https://user-images.githubusercontent.com/91827137/180645674-8bcf35f8-60e3-4298-8c6d-a7a81fef3e22.png)

## Data augmentation
- Data augmentation improves the training of the neural network by artificially adding new data through small transformations of the original data. 
- Each of the transformed train sets is saved into its pickle file. This makes possible to add different sets (or all) and explore what effect each of them has on improving accuracy.

## Design and Test a Model Architecture
### 1. Preprocessing:
1. GrayScale.
2. Lighting standardize.
3. Normalization.

### 2. Model Architecture:
* 2 Conv2D layer (filter = 60, kernel_size = (5, 5), activation = "relu")
* MaxPool2D layer (pool_size = (2, 2))
* 2 Conv2D layer (filter = 30, kernel_size = (3, 3), activation = "relu")
* MaxPool2D layer (pool_size = (2, 2))
* Dropout layer (rate = 0.5)
* Flatten layer to squeeze the layers into 1 dimension
* Dense Fully connected layer (500 nodes, activation=”relu”)
* Dropout layer (rate=0.5)
* Dense layer ( 500 nodes, activation=”softmax”)

### 3. Compilation:
loss is “categorical_crossentropy” because we have multiple classes to categorise.

```
    model = Sequential()
    model.add((Conv2D(no_of_filters, size_of_filter,
                      input_shape=(imageDimensions[0], imageDimensions[1], 1),
                      activation='relu')))  # Adding more convolution layers, fewer features but cause accuracy to increase
    model.add((Conv2D(no_of_filters, size_of_filter, activation='relu')))
    model.add(MaxPooling2D(pool_size=size_of_pool))  # Doesn't affect the depth/number of filters

    model.add((Conv2D(no_of_filters // 2, size_of_filter_2, activation='relu')))
    model.add((Conv2D(no_of_filters // 2, size_of_filter_2, activation='relu')))
    model.add(MaxPooling2D(pool_size=size_of_pool))
    model.add(Dropout(0.5))

    model.add(Flatten())
    model.add(Dense(no_of_nodes, activation='relu'))
    model.add(Dropout(0.5))  # Inputs nodes to drop with each update 1 all 0 None
    model.add(Dense(noOfClasses, activation='softmax'))  # Output layer

    # Compile model
    model.compile(Adam(lr=0.001), loss='categorical_crossentropy', metrics=['accuracy'])
    return model
```
### 4. Train and validate the model:
Training the model using `model.fit()`
`batch_size` = 50
`Accuracy` = 99%
`test_score` = 0.016

### Accuracy and Loss plotting

`Accuracy`:

![Screenshot (662)](https://user-images.githubusercontent.com/91827137/180646456-34ae2f59-c6d5-419d-be07-11e14e416ebb.png)

`Loss`:

![Screenshot (663)](https://user-images.githubusercontent.com/91827137/180646461-720c2165-ef65-4759-bae9-685f3b9ebe04.png)

# Output:

![Screenshot (671)](https://user-images.githubusercontent.com/91827137/180647256-bfbd141d-bc0a-4b1a-9a49-0d58ab262ca0.png)

![Screenshot (670)](https://user-images.githubusercontent.com/91827137/180647265-95bf72cb-ec54-4cdd-a9f1-f9c166b5fa08.png)

![Screenshot (669)](https://user-images.githubusercontent.com/91827137/180647277-f7150f53-d47c-487a-8712-4238e5bf3235.png)

# Resources:
- https://data-flair.training/blogs/python-project-traffic-signs-recognition/
- https://towardsdatascience.com/traffic-sign-detection-using-convolutional-neural-network-660fb32fe90e
- https://san-wang.github.io/blog/GTSRB_Caffe/
