# import sys
# import os
# import requests
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QFileDialog
# from PyQt5.QtGui import QPixmap, QPainter, QPen, QColor
# from PyQt5.QtCore import Qt
# import cv2

# from object_detector import ObjectDetector
# from utils import load_images, save_annotation

# # Download the pre-trained model if it doesn't exist
# MODEL_URL = 'https://download.pytorch.org/models/fasterrcnn_resnet50_fpn_coco-258fb6c6.pth'
# MODEL_PATH = 'pretrained_models/fasterrcnn_resnet50_fpn_coco.pth'

# if not os.path.exists(MODEL_PATH):
#     os.makedirs('pretrained_models', exist_ok=True)
#     print("Downloading pre-trained model...")
#     response = requests.get(MODEL_URL, stream=True)
#     with open(MODEL_PATH, 'wb') as f:
#         for chunk in response.iter_content(chunk_size=8192):
#             f.write(chunk)
#     print("Pre-trained model downloaded successfully.")

# class AnnotationGUI(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#         self.object_detector = ObjectDetector(MODEL_PATH)
#         self.image_paths = []
#         self.current_index = 0

#     def initUI(self):
#         self.setWindowTitle('Auto Annotation Tool')
#         central_widget = QWidget()
#         layout = QVBoxLayout()

#         self.image_label = QLabel()
#         self.image_label.setAlignment(Qt.AlignCenter)
#         layout.addWidget(self.image_label)

#         central_widget.setLayout(layout)
#         self.setCentralWidget(central_widget)

#         self.load_images_action = self.menuBar().addAction('Load Images')
#         self.load_images_action.triggered.connect(self.load_images)
#         self.prev_image_action = self.menuBar().addAction('Previous Image')
#         self.prev_image_action.triggered.connect(self.prev_image)
#         self.next_image_action = self.menuBar().addAction('Next Image')
#         self.next_image_action.triggered.connect(self.next_image)

#     def load_images(self):
#         image_dir = QFileDialog.getExistingDirectory(self, 'Select Image Directory')
#         if image_dir:
#             self.image_paths = load_images(image_dir)
#             self.current_index = 0
#             self.display_image()

#     def display_image(self):
#         if self.image_paths:
#             image_path = self.image_paths[self.current_index]
#             image = cv2.imread(image_path)
#             height, width, _ = image.shape
#             qimage = QPixmap.fromImage(image)
#             self.image_label.setPixmap(qimage.scaled(width, height))

#             # Detect objects and draw bounding boxes
#             predictions = self.object_detector.detect_objects(image)
#             self.draw_bounding_boxes(predictions, image)

#             # Save annotations
#             save_annotation(image_path, predictions, 'data/annotations/')

#     def draw_bounding_boxes(self, predictions, image):
#         qimage = QPixmap.fromImage(image)
#         painter = QPainter(qimage)
#         pen = QPen(QColor(255, 0, 0), 2)
#         painter.setPen(pen)

#         for prediction in predictions:
#             bbox = prediction['boxes']
#             x1, y1, x2, y2 = [int(val) for val in bbox]
#             painter.drawRect(x1, y1, x2 - x1, y2 - y1)

#         self.image_label.setPixmap(qimage.scaled(qimage.width(), qimage.height()))

#     def prev_image(self):
#         if self.current_index > 0:
#             self.current_index -= 1
#             self.display_image()

#     def next_image(self):
#         if self.current_index < len(self.image_paths) - 1:
#             self.current_index += 1
#             self.display_image()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     annotation_gui = AnnotationGUI()
#     annotation_gui.show()
#     sys.exit(app.exec_())


import sys
import os
import requests
from PyQt5.QtWidgets import QApplication
from object_detector import ObjectDetector
from main_window import MainWindow

# Download the pre-trained model if it doesn't exist
MODEL_URL = 'https://download.pytorch.org/models/fasterrcnn_resnet50_fpn_coco-258fb6c6.pth'
MODEL_PATH = 'pretrained_models/fasterrcnn_resnet50_fpn_coco.pth'

if not os.path.exists(MODEL_PATH):
    os.makedirs('pretrained_models', exist_ok=True)
    print("Downloading pre-trained model...")
    response = requests.get(MODEL_URL, stream=True)
    with open(MODEL_PATH, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    print("Pre-trained model downloaded successfully.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    object_detector = ObjectDetector(MODEL_PATH)
    main_window = MainWindow(object_detector)
    main_window.show()
    sys.exit(app.exec_())