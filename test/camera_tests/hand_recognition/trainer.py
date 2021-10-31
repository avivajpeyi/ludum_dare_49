# Importing import modules
import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
from PIL import Image
import matplotlib.pyplot as plt
import os
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from keras import optimizers
from keras.optimizers import Adam, SGD, Adagrad, Adadelta, RMSprop
from keras.utils import to_categorical
from skimage import io

print(os.listdir("../input/gestures-hand/data/data"))

#%% md
#
# The dataset is already been split into train, test and validation (so we dont need to do it later on)

#%%

# Train, test and validation directories
train_dir = "../input/gestures-hand/data/data/train"
val_dir = "../input/gestures-hand/data/data/validation"
test_dir = "../input/gestures-hand/data/data/test"

#%% md

## Exploring the dataset
#
# The dataset contains three different directories called `train`, `test` and `validation`. Each of these directories contain 7 sub-directories which essentially refer to the six types of hand gestures i.e. `five`, `fist`, `rad`, `okay`, `peace`, `straight` and `thumbs`. Additionally, there is a `none` directory which contains images of the background without any hand in it which can be used as initial background setup.
#
# All the images in the dataset have been preprocessed already via OpenCV's background subtraction algorithms by the following steps :
# * Applying smoothing filter that keeps edges sharp using `cv2.bilateralFilter`
# * Removing background like eroding background using `cv2.erode` , etc.
# * Create a background mask
# * Created a Region of Interest (ROI)
# * Converting image to gray using `cv2.cvtColor`
# * Blurring the image using `cv2.GaussianBlur`
# * Thresholding the image using `cv2.threshold`
#

#%% md

### Visualising each gesture
# Show one image of the each of the 8 classes present.

#%%

img_array1 = np.array(
    Image.open("../input/gestures-hand/data/data/train/fist/123.png")
)
plt.imshow(img_array1)

#%%

img_array2 = np.array(
    Image.open("../input/gestures-hand/data/data/train/five/123.png")
)
plt.imshow(img_array2)

#%%

img_array3 = np.array(
    Image.open("../input/gestures-hand/data/data/train/none/123.png")
)
plt.imshow(img_array3)

#%%

img_array4 = np.array(
    Image.open("../input/gestures-hand/data/data/train/okay/123.png")
)
plt.imshow(img_array4)

#%%

img_array5 = np.array(
    Image.open("../input/gestures-hand/data/data/train/peace/123.png")
)
plt.imshow(img_array5)

#%%

img_array6 = np.array(
    Image.open("../input/gestures-hand/data/data/train/rad/123.png")
)
plt.imshow(img_array6)

#%%

img_array7 = np.array(
    Image.open("../input/gestures-hand/data/data/train/straight/123.png")
)
plt.imshow(img_array7)

#%%

img_array8 = np.array(
    Image.open("../input/gestures-hand/data/data/train/thumbs/123.png")
)
plt.imshow(img_array8)

#%% md
#
# The variable `outputSize` refers to the number of different hand gestures in the dataset. Since it is a multi-class classification model, this will determine the number of units in the final dense layer preceeding the softmax activation.

#%%

# Declaring variables
outputSize = len(os.listdir(train_dir))  # nuumber of gestures
epochs = 30  # Number of epochs

#%% md

## Data Augmentation
#
# Image data augmentation is a technique that can be used to artificially expand the size of a training dataset by creating modified versions of images in the dataset.
#
# Training deep learning neural network models on more data can result in more skillful models, and the augmentation techniques can create variations of the images that can improve the ability of the fit models to generalize what they have learned to new images.
#
# The Keras deep learning neural network library provides the capability to fit models using image data augmentation via the `ImageDataGenerator` class.
#
# First, the class may be instantiated and the configuration for the types of data augmentation are specified by arguments to the class constructor.
#
# A range of techniques are supported, as well as pixel scaling methods. We will focus on five main types of data augmentation techniques for image data; specifically:
#
#  * Image shifts via the `width_shift_range` and `height_shift_range` arguments.
#  *   Image flips via the `horizontal_flip` arguments.
#  *   Image rotations via the `rotation_range` argument
#  *  Shear angle in counter-clockwise direction in degrees via the `shear_range` argument.
#  *  Image zoom via the `zoom_range `argument.


#%%

# Train Data Generator to do data augmentation on training images
train_datagen = ImageDataGenerator(
    rescale=1.0 / 255,
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
)

#%%

# Test Data Generator
test_datagen = ImageDataGenerator(rescale=1.0 / 255)

#%%

# Setting up the train generator to flow from the train directory
train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(256, 256),
    batch_size=32,
    class_mode="categorical",
    color_mode="grayscale",
)

# Doing the same as above for the validation directory
val_generator = test_datagen.flow_from_directory(
    val_dir,
    target_size=(256, 256),
    batch_size=32,
    class_mode="categorical",
    color_mode="grayscale",
)

#%% md

## Defining the CNN


#%%

# Function to create keras model for different number of gestures
def create_model(outputSize):
    model = Sequential()
    model.add(
        Conv2D(
            filters=32,
            kernel_size=(3, 3),
            activation="relu",
            input_shape=(256, 256, 1),
        )
    )
    model.add(Conv2D(filters=32, kernel_size=(3, 3), activation="relu"))
    model.add(MaxPooling2D(pool_size=2))
    model.add(Conv2D(filters=64, kernel_size=(3, 3), activation="relu"))
    model.add(Conv2D(filters=64, kernel_size=(3, 3), activation="relu"))
    model.add(MaxPooling2D(pool_size=2))
    model.add(Conv2D(filters=128, kernel_size=(3, 3), activation="relu"))
    model.add(Conv2D(filters=128, kernel_size=(3, 3), activation="relu"))
    model.add(MaxPooling2D(pool_size=2))
    model.add(Flatten())
    model.add(Dropout(rate=0.5))
    model.add(Dense(512, activation="relu"))
    model.add(Dense(units=outputSize, activation="softmax"))
    model.compile(
        optimizer=Adam(lr=1e-4),
        loss="categorical_crossentropy",
        metrics=["accuracy"],
    )
    return model


#%%

# Creating the model
model = create_model(outputSize)

#%%

# Summary of model
model.summary()

#%%

import tensorflow as tf

tf.keras.utils.plot_model(model, show_shapes=True)

#%%

# Fitting the model to the data based on a 32 batch size
history = model.fit_generator(
    train_generator,
    steps_per_epoch=outputSize * 1000 / 32,
    epochs=epochs,
    validation_data=val_generator,
    validation_steps=outputSize * 500 / 32,
)

#%% md

## Results and Performance Metrics

#%%

# Plotting training acc/loss and val acc/loss
acc = history.history["accuracy"]
val_acc = history.history["val_accuracy"]
loss = history.history["loss"]
val_loss = history.history["val_loss"]
range_ep = epochs + 1
epoch_x = range(1, range_ep)

plt.plot(epoch_x, acc, "bo", label="Training Acc")
plt.plot(epoch_x, val_acc, "b", label="Validation Acc")
plt.title("Training and Validation Acc")
plt.legend()
plt.figure()

plt.plot(epoch_x, loss, "bo", label="Training Loss")
plt.plot(epoch_x, val_loss, "b", label="Validation Loss")
plt.title("Training and Validation Loss")
plt.legend()
plt.figure()

plt.show()

#%%

# Setting up the test generator to flow from the test directory
test_generator = test_datagen.flow_from_directory(
    test_dir,
    target_size=(256, 256),
    batch_size=32,
    class_mode="categorical",
    color_mode="grayscale",
)

#%%

# Test accuracy and test loss calc
test_loss, test_acc = model.evaluate_generator(
    test_generator, steps=outputSize * 500 / 32
)
print("Test Acc:", test_acc)
print("Test Loss:", test_loss)

#%% md

## Saving Model and Model Weights
#
# Model progress can be saved during and after training. This means a model can resume where it left off and avoid long training times. Saving also means you can share your model and others can recreate your work. When publishing research models and techniques, most machine learning practitioners share:
#
#   * code to create the model, and
#   * the trained weights, or parameters, for the model
#

#%%

# Model weights and model
model.save_weights("gesture_model_weights.h5")
model.save("gesture_model.h5")


## Future Work
#
# The model can be improved by
# - reducing overfitting by earlystopping
# - random train test split
