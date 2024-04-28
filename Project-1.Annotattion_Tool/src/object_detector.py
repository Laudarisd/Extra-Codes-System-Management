import torch

class ObjectDetector:
    def __init__(self, model_path=None, model_name='yolov8'):
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        
        # Load YOLOv8 model; adjust this according to your YOLOv8 implementation
        if model_path:  # If a custom model path is provided
            self.model = torch.load(model_path, map_location=self.device)
        else:  # Load default YOLOv8 model
            self.model = torch.hub.load('ultralytics/yolov8', model_name, pretrained=True)
        
        self.model.to(self.device)
        self.model.eval()

    def detect_objects(self, image):
        # Convert image from OpenCV BGR to RGB format
        image = image[:, :, ::-1]

        # Inference
        results = self.model(image)

        # Parse results
        detected_objects = []
        for *xyxy, conf, cls in results.xyxy[0]:  # xyxy, confidence and class
            detected_objects.append({
                'boxes': xyxy,
                'score': conf.item(),
                'category': self.model.names[int(cls)]
            })

        return detected_objects
