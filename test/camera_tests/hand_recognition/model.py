# Importing Modules
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (
    Conv2D,
    MaxPooling2D,
    Flatten,
    Dense,
    Dropout,
)
from tensorflow.keras import optimizers

from .constants import *


# Creating our deep learning model to recognize the hand image
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
        optimizer=optimizers.Adam(),
        loss="categorical_crossentropy",
        metrics=["accuracy"],
    )

    return model


# Function to load the model
def load_model(outputSize, weight_url):
    # Loading the model
    modelName = "Hand Gesture Recognition"
    print(f"Loading model {modelName}")
    model = create_model(NUMBEROFGESTURES)
    model.load_weights(weight_url)

    return model, modelName
