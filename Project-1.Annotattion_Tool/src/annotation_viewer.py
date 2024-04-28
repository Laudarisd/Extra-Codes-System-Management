from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap, QPainter, QPen, QColor
from PyQt5.QtCore import Qt

class AnnotationViewer(QLabel):
    def __init__(self, object_detector):
        super().__init__()
        self.object_detector = object_detector
        self.setAlignment(Qt.AlignCenter)
        self.predictions = []

    def displayAnnotations(self, image_path):
        image = cv2.imread(image_path)
        predictions = self.object_detector.detect_objects(image)
        self.predictions = predictions
        self.drawAnnotations(image, predictions)

    def drawAnnotations(self, image, predictions):
        qimage = QPixmap.fromImage(image)
        painter = QPainter(qimage)
        pen = QPen(QColor(255, 0, 0), 2)
        painter.setPen(pen)

        for prediction in predictions:
            bbox = prediction['boxes']
            x1, y1, x2, y2 = [int(val) for val in bbox]
            painter.drawRect(x1, y1, x2 - x1, y2 - y1)

        self.setPixmap(qimage.scaled(qimage.width(), qimage.height()))