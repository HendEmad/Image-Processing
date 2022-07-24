# Import modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import pickle
import random
import cv2
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from keras.utils.np_utils import to_categorical
from keras.layers import Dropout, Flatten
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split

# Parameters
path = "myData"  # Folder with all the class folders
labelFile = "labels.csv"  # File with all names of classes
batch_size_val = 50  # How many to process together
steps_per_epoch_val = 2000
epochs_val = 10  # How many iterations it will go through. The higher, the longer execution, the better results
imageDimensions = (32, 32, 3)  # Height, Width, Channels
testRatio = 0.2  # If 1000 images, split 200 for testing, 800 remain
validationRatio = 0.2  # If 1000 images & 20% of remaining 800 will be for validation(160 images of 800)

# Importing images
# This code will automatically detect how many classes in the data, once we uploaded it
# It will but the classes together in one matrix
count = 0
images = []
classNumber = []
myList = os.listdir(path)
print("Total number of classes: ", len(myList))
noOfClasses = len(myList)
print("Importing classes.......")
for x in range(len(myList)):
    PicList = os.listdir(path + "/" + str(count))
    for y in PicList:
        curImg = cv2.imread(path + "/" + str(count) + "/" + y)
        images.append(curImg)
        classNumber.append(count)
    print(count, end=" ")
    count += 1
print(" ")
images = np.array(images)
classNumber = np.array(classNumber)

# Split data
x_train, x_test, y_train, y_test = train_test_split(images, classNumber, test_size=testRatio)
x_train, x_validation, y_train, y_validation = train_test_split(x_train, y_train, test_size=validationRatio)

# Test if number of images matches to the number of labels for each dataset
print("Data Shapes")
print("Train", end="");
print(x_train.shape, y_train.shape)
print("Validation", end="");
print(x_validation.shape, y_validation.shape)
print("Test", end="");
print(x_test.shape, y_test.shape)
assert (x_train.shape[0] == y_train.shape[
    0]), "The number of images in not equal to the number of labels in training set"
assert (x_validation.shape[0] == y_validation.shape[
    0]), "The number of images in not equal to the number of labels in validation set"
assert (x_test.shape[0] == y_test.shape[0]), "The number of images in not equal to the number of labels in test set"
assert (x_train.shape[1:] == imageDimensions), " The dimensions of the Training images are wrong "
assert (x_validation.shape[1:] == imageDimensions), " The dimensions of the Validation images are wrong "
assert (x_test.shape[1:] == imageDimensions), " The dimensions of the Test images are wrong"

# Read csv file
data = pd.read_csv(labelFile)
print("data shape", data.shape, type(data))

# display some samples images of all the classes
num_of_samples = []
cols = 5
num_classes = noOfClasses
fig, axs = plt.subplots(nrows=num_classes, ncols=cols, figsize=(5, 300))
fig.tight_layout()
for i in range(cols):
    for j, row in data.iterrows():
        x_selected = x_train[y_train == j]
        axs[j][i].imshow(x_selected[random.randint(0, len(x_selected) - 1), :, :], cmap=plt.get_cmap("gray"))
        axs[j][i].axis("off")
        if i == 2:
            axs[j][i].set_title(str(j) + "-" + row["Name"])
            num_of_samples.append(len(x_selected))

# display a bar chart for samples of each category
print(num_of_samples)
plt.figure(figsize=(12, 4))
plt.bar(range(0, num_classes), num_of_samples)
plt.title("Distribution of the training dataset")
plt.xlabel("Class number")
plt.ylabel("Number of images")
plt.show()

''' comment on the distribution:
we don't have the same number of images for each class(not normally distributed)
# This leads to a good classification for one class and bad classification for another one
# This means we don't have enough data for each class.
'''


# Images preprocessing

def grayScale(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img


def equalize(img):
    img = cv2.equalizeHist(img)
    return img


def preprocessing(img):
    img = grayScale(img)  # convert to grayscale
    img = equalize(img)  # standardize the lighting in the image
    img = img / 255  # to normalize values between 0 and 1 instead of 0 and 255
    return img


x_train = np.array(list(map(preprocessing, x_train)))  # To iterate and preprocess all images
x_validation = np.array(list(map(preprocessing, x_validation)))
x_test = np.array(list(map(preprocessing, x_test)))
cv2.imshow("GrayScale Images", x_train[random.randint(0, len(x_train) - 1)])  # To check if the training is done

# Add a depth of 1
x_train = x_train.reshape(x_train.shape[0], x_train.shape[1], x_train.shape[2], 1)
x_validation = x_validation.reshape(x_validation.shape[0], x_validation.shape[1], x_validation.shape[2], 1)
x_test = x_test.reshape(x_test.shape[0], x_test.shape[1], x_test.shape[2], 1)

# Augmentation of images; to make it more generic
dataGen = ImageDataGenerator(width_shift_range=0.1,
                             # 0.1 = 10%     if more than 1 E.G 10 then ir refers to number of pixels E.G 10 to pixels
                             height_shift_range=0.1,
                             zoom_range=0.2,  # 0.2 means can go from 0.8 to 1.2
                             shear_range=0.1,  # magnitude of shear angle
                             rotation_range=10)  # degrees
dataGen.fit(x_train)
batches = dataGen.flow(x_train, y_train,
                       batch_size=20)  # requesting data generator to generate images batch size = number of images created each time it is called
x_batch, y_batch = next(batches)

# to show augmented image samples
fig, axs = plt.subplots(1, 15, figsize=(20, 5))
fig.tight_layout()
for i in range(15):
    axs[i].imshow(x_batch[i].reshape(imageDimensions[0], imageDimensions[1]))
    axs[i].axis('off')
plt.show()

y_train = to_categorical(y_train, noOfClasses)
y_validation = to_categorical(y_validation, noOfClasses)
y_test = to_categorical(y_test, noOfClasses)


# Convolution Neural Network model
# Lynette model, a few convolutional layers, few of the pooling, and few drop out layers
# Dense layer ---> output layer
def model():
    no_of_filters = 60
    size_of_filter = (5, 5)  # a kernel that move around the image to get the features.
    # this kernel would remove 2 pixels from each border when using 32 32 image
    size_of_filter_2 = (3, 3)
    size_of_pool = (2, 2)  # scake down all feature map to generalize more; to reduce Overfitting
    no_of_nodes = 500  # number of nodes in hidden layers
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

# Training
model = model()
print(model.summary())
history = model.fit_generator(dataGen.flow(x_train, y_train, batch_size= batch_size_val), steps_per_epoch=steps_per_epoch_val, epochs=epochs_val, validation_data=(x_validation, y_validation), shuffle=1)

# Plotting
plt.figure(1)
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.legend(['training', 'validation'])
plt.title('loss')
plt.xlabel('epoch')
plt.figure(2)
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.legend(['training', 'validation'])
plt.title('Accuracy')
plt.xlabel('epoch')
plt.show()
score =model.evaluate(x_test, y_test, verbose=0)
print('Test Score:', score[0])
print('Test Accuracy:', score[1])

# Store the model as a pickle object
pickle_out = open("model_trained.p", "wb")  # wb = WRITE BYTE
pickle.dump(model, pickle_out)
pickle_out.close()
cv2.waitKey(0)