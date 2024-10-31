# face-Detection-using-YOLO

## Overview

The Face Detector Application is a real-time face detection tool developed using PySide6, OpenCV, and the YOLOv8 model. This application captures live video from a webcam, detects faces, and displays confidence scores. It features a user-friendly interface that allows users to start and stop the camera easily.

## Features

- **Real-Time Face Detection**: Utilizes YOLOv8 to detect faces in live video.
- **User Interface**: Built with PySide6 for a clean and intuitive experience.
- **Dynamic Status Updates**: Displays the current status of the camera.
- **Confidence Scores**: Shows confidence values for detected faces.

## Technical Stack

- **Programming Language**: Python
- **Libraries and Frameworks**:
  - [PySide6](https://pypi.org/project/PySide6/) for creating the GUI
  - [OpenCV](https://opencv.org/) for video processing
  - [Ultralytics YOLOv8](https://github.com/ultralytics/yolov5) for face detection

## Installation

### Prerequisites

Make sure you have Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Step 1: Clone the Repository

```bash
git clone https://github.com/prajwal2431/face-Detection-using-YOLO.git
cd face-Detection-using-YOLO
```

### Step 2: Install Required Packages

You can install the required packages using pip:

```bash
pip install -r requirements.txt
```

### Step 3: Download YOLOv8 Model

Make sure to download the `yolov8n.pt` model file and place it in the project directory. You can find the model weights [here](https://github.com/ultralytics/yolov5/releases).

## Usage

1. Run the application:

   ```bash
   python faceDetectorApp.py
   ```

2. Select the desired camera from the dropdown menu.
3. Click the "Start" button to begin face detection.
4. Click the "Stop" button to stop the camera feed.

## Future Enhancements

- **Facial Recognition**: Integrate facial recognition capabilities to identify individuals.
- **Emotion Detection**: Analyze facial expressions to determine emotions.


## Contact

For any questions or feedback, please reach out to me at [prajwalnivangune914@gmail.com].

