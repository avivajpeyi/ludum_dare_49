"""
GLOBAL VARIABLES
"""
# Layout/FrontEnd of Frame
IMAGEHEIGHT = 480
IMAGEWIDTH = 640
ROIWIDTH = 256
LEFT = int(IMAGEWIDTH / 2 - ROIWIDTH / 2)
RIGHT = LEFT + ROIWIDTH
TOP = int(IMAGEHEIGHT / 2 - ROIWIDTH / 2)
BOTTOM = TOP + ROIWIDTH
SCOREBOXWIDTH = 320
BARCHARTLENGTH = SCOREBOXWIDTH - 50
BARCHARTTHICKNESS = 15
BARCHARTGAP = 20
BARCHARTOFFSET = 8
FONT = cv2.FONT_HERSHEY_SIMPLEX

# Model variables
NUMBEROFGESTURES = 8
WEIGHTS_URL = "./my_model.h5"
GESTURE_ENCODING = {
    0: "fist",
    1: "five",
    2: "none",
    3: "okay",
    4: "peace",
    5: "rad",
    6: "straight",
    7: "thumbs",
}

# OpenCV image processing variables
BGSUBTHRESHOLD = 50
THRESHOLD = 50

# Gesture Mode variables
GESTUREMODE = False  # Don't ever edit this!
GESTURES_RECORDED = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
SONG = "The Beatles - I Saw Her Standing There"
ACTIONS_GESTURE_ENCODING = {
    "fist": "Play/Unpause",
    "five": "Pause",
    "none": "Do Nothing",
    "okay": "Increase Volume",
    "peace": "Decrease Volume",
    "rad": "Load Song",
    "straight": "Stop",
    "thumbs": "NA",
}

# Data Collection Mode variables
DATAMODE = True  # Don't ever edit this!
WHERE = "train"
GESTURE = "okay"
NUMBERTOCAPTURE = 100

# Testing Predictions of Model Mode variables
PREDICT = False  # Don't ever edit this!
HISTORIC_PREDICTIONS = [
    np.ones((1, 8)),
    np.ones((1, 8)),
    np.ones((1, 8)),
    np.ones((1, 8)),
    np.ones((1, 8)),
]
IMAGEAVERAGING = 5
