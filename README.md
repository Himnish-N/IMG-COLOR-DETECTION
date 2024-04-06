# IMG-COLOR-DETECTION
using opencv with python to detect the colour of different images using a web cam


## Overview
This Python script captures video from the webcam using OpenCV and retrieves the pixel values of the center of the captured frame in HSV color space.

## Requirements
- Python 3.x
- OpenCV (cv2) library

## Usage
1. Make sure you have Python installed on your system.
2. Install the OpenCV library by running the following command:
    ```
    pip install opencv-python
    ```
3. Connect your webcam to your computer.
4. Run the script `color_recognition.py`.
5. The script will open a window displaying the video feed from the webcam.
6. The script will print the HSV pixel values of the center of the video frame.
7. Press `Esc` key to exit the script.

## Additional Notes
- You can change the webcam index by modifying the argument of `cv2.VideoCapture()` function. Default index is 0.
- You can adjust the width and height of the video frame by changing the values passed to `cap.set(cv2.CAP_PROP_FRAME_WIDTH, ...)` and `cap.set(cv2.CAP_PROP_FRAME_HEIGHT, ...)`.
- The pixel values are printed in the format `(H, S, V)`, where `H` represents the Hue, `S` represents the Saturation, and `V` represents the Value.
