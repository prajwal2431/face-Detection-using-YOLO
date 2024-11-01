# Face Detector Application 🎉

## Overview
This project is my first step into the world of Computer Vision and Artificial Intelligence! It’s a Face Detector application developed using **PySide6**, **OpenCV**, and **YOLOv8**, with additional emotion detection powered by **DeepFace**. The application captures live video, detects faces in real-time, and displays personalized greetings based on detected emotions.

## Features
- **Real-Time Face Detection**: Utilizes YOLOv8 for detecting faces in real-time from the live camera feed.
- **Emotion-Based Greetings**: Displays a message depending on the detected emotion:
  - 😊 **Happy**: Displays “Happy Laxmi Pujan!”
  - 😔 **Sad/Other**: Encourages the user with "Smile, it's Laxmi Pujan!"
- **User-Friendly Interface**: Built with PySide6 for a clean and interactive GUI.
- **Dynamic Status Updates**: Users can easily start and stop the camera feed, with status messages reflecting the application's state.

## Technical Stack
- **Programming Language**: Python
- **Libraries**:
  - **PySide6**: For building a responsive GUI
  - **OpenCV**: For video capture and image processing
  - **YOLOv8**: Used for face detection
  - **DeepFace**: Used for emotion detection

## Setup and Installation
To run this project, make sure you have Python installed. Follow the steps below to set up your environment:

1. Clone the repository:
   ```bash
   git clone https://github.com/prajwal2431/face-Detection-using-YOLO.git
   cd face-Detection-using-YOLO
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python faceDetectorApp.py
   ```

## How It Works
1. **Start the Camera**: When the "Start" button is pressed, the application captures video from the camera.
2. **Face Detection**: YOLOv8 detects faces in the frame, and each face is highlighted with a bounding box.
3. **Emotion Detection**: Using DeepFace, each detected face is analyzed to determine the dominant emotion.
4. **Personalized Message**: A greeting message is displayed based on the emotion detected:
   - **Happy**: “Happy Laxmi Pujan!”
   - **Other Emotions**: “Smile, it’s Laxmi Pujan!”

## Future Enhancements
- **Facial Recognition**: Identify and greet known individuals by name.
- **Enhanced Emotion Analysis**: Support additional emotions and customize greetings.
- **Additional Camera Options**: Allow for video file input or multiple camera sources.

## Example Usage
1. **Start the Application**: Launch the app and press "Start" to begin face detection.
2. **View Greetings**: Smile to receive a festive greeting, or make a neutral face to get a prompt to smile!
3. **Stop the Application**: Press "Stop" to end the camera feed and close the app.

## Requirements
The application requires the following Python libraries (provided in `requirements.txt`):
- `PySide6`
- `opencv-python`
- `ultralytics`
- `numpy`
- `deepface`

## Contributing
Feel free to fork the repository and submit pull requests for any enhancements or bug fixes!



---

Happy Coding and Happy Laxmi Pujan! 🪔