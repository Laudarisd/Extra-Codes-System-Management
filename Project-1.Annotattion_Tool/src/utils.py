import os
import cv2
import xml.etree.ElementTree as ET

def load_images(directory):
    """
    Loads image paths from a directory.

    Args:
        directory (str): Path to the directory containing images.

    Returns:
        list: List of image paths.
    """
    image_paths = []
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path) and file_name.lower().endswith(('.jpg', '.png', '.bmp')):
            image_paths.append(file_path)
    return image_paths

def save_annotation(image_path, predictions, output_dir):
    """
    Saves object detection annotations in PASCAL VOC format.

    Args:
        image_path (str): Path to the image file.
        predictions (list): List of dictionaries containing object predictions.
        output_dir (str): Path to the output directory for saving annotations.
    """
    image_name = os.path.splitext(os.path.basename(image_path))[0]
    annotation_path = os.path.join(output_dir, f"{image_name}.xml")

    image = cv2.imread(image_path)
    height, width, _ = image.shape

    root = ET.Element("annotation")

    folder = ET.SubElement(root, "folder")
    folder.text = "images"

    filename = ET.SubElement(root, "filename")
    filename.text = os.path.basename(image_path)

    source = ET.SubElement(root, "source")
    database = ET.SubElement(source, "database")
    database.text = "Unknown"

    size = ET.SubElement(root, "size")
    width_elem = ET.SubElement(size, "width")
    width_elem.text = str(width)
    height_elem = ET.SubElement(size, "height")
    height_elem.text = str(height)
    depth_elem = ET.SubElement(size, "depth")
    depth_elem.text = "3"

    segmented = ET.SubElement(root, "segmented")
    segmented.text = "0"

    for prediction in predictions:
        object_elem = ET.SubElement(root, "object")
        name = ET.SubElement(object_elem, "name")
        name.text = prediction["category"]
        pose = ET.SubElement(object_elem, "pose")
        pose.text = "Unspecified"
        truncated = ET.SubElement(object_elem, "truncated")
        truncated.text = "0"
        difficult = ET.SubElement(object_elem, "difficult")
        difficult.text = "0"
        bndbox = ET.SubElement(object_elem, "bndbox")
        xmin = ET.SubElement(bndbox, "xmin")
        xmin.text = str(prediction["boxes"][0])
        ymin = ET.SubElement(bndbox, "ymin")
        ymin.text = str(prediction["boxes"][1])
        xmax = ET.SubElement(bndbox, "xmax")
        xmax.text = str(prediction["boxes"][2])
        ymax = ET.SubElement(bndbox, "ymax")
        ymax.text = str(prediction["boxes"][3])

    tree = ET.ElementTree(root)
    os.makedirs(output_dir, exist_ok=True)
    tree.write(annotation_path)