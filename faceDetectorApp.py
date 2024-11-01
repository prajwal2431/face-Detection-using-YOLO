import sys
import cv2
import numpy as np
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer
from PySide6.QtGui import QImage, QPixmap
from facedetector_ui import Ui_MainWindow
from ultralytics import YOLO
from deepface import DeepFace

class FaceDetectorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.cap = None
        self.timer = QTimer()

        self.setStyleSheet("background-color: #D1E8FF;")  

        self.ui.startButton.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;  
                color: white;
                border: none;
                padding: 10px;
                font-size: 16px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #45a049; 
            }
            QPushButton:pressed {
                background-color: #388e3c;  
            }
        """)

        self.ui.stopButton.setStyleSheet("""
            QPushButton {
                background-color: #f44336; 
                color: white;
                border: none;
                padding: 10px;
                font-size: 16px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #e53935;  
            }
            QPushButton:pressed {
                background-color: #c62828;  
            }
        """)

        # Status box
        self.ui.statusBox.setStyleSheet("background-color: #ffffff; color: black;")  

        # Load YOLOv8 model
        self.model = YOLO('yolov8n.pt') 
        
        # Connect buttons to functions
        self.ui.startButton.clicked.connect(self.start_camera)
        self.ui.stopButton.clicked.connect(self.stop_camera)
        self.timer.timeout.connect(self.update_frame)
        
    def start_camera(self):
        self.cap = cv2.VideoCapture(0)
        
        if not self.cap.isOpened():
            self.update_status("Error: Unable to open camera.")
            return
        self.update_status("Camera started.")
        self.timer.start(10)  # Update frame every 10ms
    
    def stop_camera(self):
        self.timer.stop()
        
        if self.cap is not None:
            self.cap.release()
        self.update_status("Camera stopped.")
    
    def update_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            self.update_status("Failed to retrieve frame.")
            return

        # Perform inference on the frame
        results = self.model(frame)

        # Loop through results and draw bounding boxes
        for result in results[0].boxes:
            # Get bounding box coordinates
            x1, y1, x2, y2 = map(int, result.xyxy[0])
            # Draw rectangle on frame
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            # Display confidence score
            conf = result.conf[0]
            cv2.putText(frame, f"{conf:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # Crop the detected face for emotion analysis
            face = frame[y1:y2, x1:x2]
            if face.size != 0:  # Ensure that the face is not empty
                # Analyze emotion using DeepFace
                try:
                    emotion = DeepFace.analyze(face, actions=['emotion'], enforce_detection=False)
                    dominant_emotion = emotion[0]['dominant_emotion']

                    # Check for smile and update message
                    if dominant_emotion == 'happy':
                        message = "Happy Laxmi Pujan!"
                    else:
                        message = "Smile, it's Laxmi Pujan!"

                    # Display the message on the frame
                    cv2.putText(frame, message, (x1, y1 - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

                except Exception as e:
                    print("Emotion analysis error:", e)

        # Convert frame to QImage and display
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = frame.shape
        bytes_per_line = ch * w
        q_img = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
        self.ui.videoLabel.setPixmap(QPixmap.fromImage(q_img))

    def update_status(self, message):
        self.ui.statusBox.setText(message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FaceDetectorApp()
    window.show()
    sys.exit(app.exec())
