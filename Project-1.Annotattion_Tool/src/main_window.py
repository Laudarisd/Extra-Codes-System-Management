from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog, QVBoxLayout, QWidget, QPushButton, QHBoxLayout
from PyQt5.QtGui import QIcon
import sys
import cv2
from image_viewer import ImageViewer  # Make sure this is correctly implemented
from annotation_viewer import AnnotationViewer  # Ensure this component is correctly implemented with clearAnnotations method
from utils import load_images, save_annotation  # Ensure these functions are correctly implemented
from object_detector import ObjectDetector  # Adjust this import based on your object detector implementation
from clear_annotation import AnnotationViewer  # Ensure this component is correctly implemented with clearAnnotations methodss



class MainWindow(QMainWindow):
    def __init__(self, object_detector):
        super().__init__()
        self.object_detector = object_detector
        self.image_path = None
        self.image_paths = []
        self.current_index = 0

        self.initUI()
        self.initComponents()

    def initUI(self):
        self.setWindowTitle('Auto Annotation Tool')
        self.setGeometry(100, 100, 800, 600)

        open_file_action = QAction(QIcon('open_file.png'), 'Open &File', self)
        open_file_action.setShortcut('Ctrl+O')
        open_file_action.triggered.connect(self.openFile)

        open_folder_action = QAction(QIcon('open_folder.png'), 'Open &Folder', self)
        open_folder_action.setShortcut('Ctrl+F')
        open_folder_action.triggered.connect(self.openFolder)

        save_action = QAction(QIcon('save.png'), '&Save', self)
        save_action.setShortcut('Ctrl+S')
        save_action.triggered.connect(self.saveAnnotations)

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&File')
        file_menu.addAction(open_file_action)
        file_menu.addAction(open_folder_action)
        file_menu.addAction(save_action)

    def initComponents(self):
        central_widget = QWidget()
        layout = QVBoxLayout()

        self.image_viewer = ImageViewer()
        self.annotation_viewer = AnnotationViewer(self.object_detector)

        button_layout = QHBoxLayout()
        self.create_annotations_button = QPushButton('Create Auto Annotations')
        self.create_annotations_button.clicked.connect(self.createAutoAnnotations)
        button_layout.addWidget(self.create_annotations_button)

        layout.addWidget(self.image_viewer)
        layout.addWidget(self.annotation_viewer)
        layout.addLayout(button_layout)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def openFile(self):
        image_path, _ = QFileDialog.getOpenFileName(self, 'Open Image', '', 'Image Files (*.png *.jpg *.bmp)')
        if image_path:
            self.image_paths = [image_path]
            self.current_index = 0
            self.display_image()

    def openFolder(self):
        folder_path = QFileDialog.getExistingDirectory(self, 'Open Folder', '')
        if folder_path:
            self.image_paths = load_images(folder_path)
            self.current_index = 0
            self.display_image()

    def display_image(self):
        if self.image_paths:
            self.image_path = self.image_paths[self.current_index]
            self.image_viewer.loadImage(self.image_path)
            self.annotation_viewer.clearAnnotations()

    def createAutoAnnotations(self):
        if self.image_path:
            image = cv2.imread(self.image_path)
            predictions = self.object_detector.detect_objects(image)
            self.annotation_viewer.displayAnnotations(image, predictions)

    def saveAnnotations(self):
        if self.image_path:
            predictions = self.annotation_viewer.get_predictions()
            save_annotation(self.image_path, predictions, 'data/annotations/')

# if __name__ == "__main__":
#     app = QApplication(sys.argv)

#     object_detector = ObjectDetector("./pretrained_models/fasterrcnn_resnet50_fpn_coco.pth")  # Adjust this according to your ObjectDetector initialization
#     window = MainWindow(object_detector)
#     window.show()

#     sys.exit(app.exec_())
            
if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Check command line arguments for a model path
    model_path = 'best.pt'  # Default model path
    if len(sys.argv) > 1:
        model_path = sys.argv[1]

    object_detector = ObjectDetector(model_path)
    main_window = MainWindow(object_detector)
    main_window.show()
    sys.exit(app.exec_())
