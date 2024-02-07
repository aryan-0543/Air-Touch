# Air-Touch
# Real-time Hand Detection and Landmark Tracking

This Python script utilizes the `mediapipe` library along with `cv2` (OpenCV) to perform real-time hand detection and landmark tracking from a webcam feed.

## Usage

Install dependencies:

```bash
pip install opencv-python mediapipe
<!-- End of installation instructions -->

Run the script:
python HandTrackingModule.py


This Python script utilizes the mediapipe library to perform real-time hand detection and landmark tracking from webcam feed using the cv2 (OpenCV) library.

The handDetector class is defined to encapsulate the functionality of hand detection and landmark tracking. The constructor initializes the hand detection model with specified parameters such as mode, maxHands, modelComplexity, detectionCon, and trackCon. The findHands method processes the input image to detect hands and draws landmarks on the image if specified. The findPosition method extracts the landmark positions for each detected hand and returns them as a list.

In the main function, a video capture object is created to access the webcam feed. An instance of the handDetector class is then created. Inside the main loop, each frame from the webcam feed is processed to detect hands and track landmarks. The landmark positions are printed to the console, and the frame is displayed with the FPS (Frames Per Second) information. The loop continues until the user exits by pressing the 'q' key.

This script can be used for various applications such as gesture recognition, sign language translation, and virtual touch interfaces.
