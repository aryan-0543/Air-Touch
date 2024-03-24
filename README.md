# Air-Touch

Air-Touch is a Python script that implements an AI-based mouse controller using hand landmarks detected from a webcam feed. It utilizes the `mediapipe` library along with `OpenCV` for hand detection and `autopy` for mouse cursor control, providing real-time interaction through hand gestures.

## Features

- **Hand Detection:** Detects hands in real-time from webcam feed.
- **Landmark Tracking:** Tracks landmarks of detected hands.
- **Cursor Control:** Controls the mouse cursor based on hand movements.
- **Click Simulation:** Simulates mouse clicks based on hand gestures.
- **Hold and Drag:** Allows holding and dragging functionality using hand gestures.
- **FPS Display:** Real-time Frames Per Second (FPS) information displayed.

## Usage

### Installation

You need to install the required dependencies first:

```
pip install opencv-python mediapipe autopy
```


### Running the Script

To run the script, execute the following command:
```
python HandTracking.py
```


Position your hand in front of the webcam to control the mouse cursor.

### Hand Gestures

- **Cursor Control:** Move your hand to move the mouse cursor.
- **Left Click:** Raise your index finger to perform a left-click.
- **Right Click:** Raise your thumb and index finger together to perform a right-click.
- **Hold and Drag:** Raise your index, middle, and ring fingers together to hold and drag.

### Exiting the Script

To exit the script, press the 'q' key.

## File Structure

- **AirTouch.py:** Main script file for running the AI-based mouse controller.
- **AirTouchModule.py:** Module containing the hand detection and landmark tracking functionalities.
- **HandTracking.py:** Script file for hand tracking and cursor control.

## About

This project demonstrates the integration of hand gesture recognition with mouse cursor control, enabling users to interact with their computer in a more intuitive and natural way. It can be further extended for various applications such as gesture-based gaming, virtual touch interfaces, and accessibility solutions.

Feel free to explore, contribute, and enhance this project for your specific needs and applications. If you encounter any issues or have suggestions for improvement, please create a GitHub issue or pull request.


