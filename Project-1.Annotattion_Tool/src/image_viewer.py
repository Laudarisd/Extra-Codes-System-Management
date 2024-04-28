from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt
import cv2
import numpy as np

class ImageViewer(QLabel):
    def __init__(self):
        super().__init__()
        self.setAlignment(Qt.AlignCenter)

    def loadImage(self, image_path):
        # Read the image using OpenCV
        image = cv2.imread(image_path)
        # Convert the image from BGR to RGB (OpenCV uses BGR by default)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        height, width, channel = image.shape

        # Create a QImage from the NumPy array
        bytesPerLine = 3 * width
        qImage = QImage(image.data, width, height, bytesPerLine, QImage.Format_RGB888)

        # Create a QPixmap from the QImage
        pixmap = QPixmap.fromImage(qImage)

        # Scale the QPixmap to fit the QLabel and set it as the pixmap
        self.setPixmap(pixmap.scaled(self.width(), self.height(), Qt.KeepAspectRatio))
