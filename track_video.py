import os
from ultralytics import YOLO

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print("Project Folder :", BASE_DIR)

model = YOLO(os.path.join(BASE_DIR, "best.pt"))

results = model.track(
    source=os.path.join(BASE_DIR, "jam-lancar.mp4"),
    tracker="bytetrack.yaml",
    persist=True,
    save=True,
    conf=0.25,
    project=os.path.join(BASE_DIR, "hasil-tracking"),
    name="jam-lancar"
)

print("Tracking Berhasil")