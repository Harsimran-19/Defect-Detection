from pathlib import Path
import sys


file_path = Path(__file__).resolve()

# Get the parent directory of the current file
root_path = file_path.parent

# Add the root path to the sys.path list if it is not already there
if root_path not in sys.path:
    sys.path.append(str(root_path))

# Get the relative path of the root directory with respect to the current working directory
ROOT = root_path.relative_to(Path.cwd())


# Source
SOURCES_LIST = ["Image", "Video", "Webcam"]


# DL model config
DETECTION_MODEL_DIR = ROOT / 'weights'/'Detection'
#YOLOv8n = DETECTION_MODEL_DIR / "yolov8n.pt"
#YOLOv8s = DETECTION_MODEL_DIR / "yolov8s.pt"
#YOLOv8m = DETECTION_MODEL_DIR / "yolov8m.pt"
#YOLOv8l = DETECTION_MODEL_DIR / "yolov8l.pt"
#YOLOv8x = DETECTION_MODEL_DIR / "yolov8x.pt"
YOLOV8custom1 = DETECTION_MODEL_DIR /"Rust.pt"
YOLOV8custom2 = DETECTION_MODEL_DIR / "Scratch.pt"
YOLOV8custom3 = DETECTION_MODEL_DIR / "Fabric.pt"
YOLOV8custom4 = DETECTION_MODEL_DIR / "Wepon.pt"

# If You Want To Use This Pre Train Model Then UnComment It and  uplode in your weights/detection dir and Use Them All

DETECTION_MODEL_LIST = [
    #"yolov8n.pt",
    #"yolov8s.pt",
    #"yolov8m.pt",
    #"yolov8l.pt",
    #"yolov8x.pt",
    "Rust.pt",
    "Scratch.pt",
    "Fabric.pt",
    "Wepon.pt"
    ]