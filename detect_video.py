import os
from ultralytics import YOLO

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print(BASE_DIR)

model = YOLO(os.path.join(BASE_DIR, "best.pt"))

results = model.predict(
    source=os.path.join(BASE_DIR, "jam-lancar.mp4"),
    save=True,
    project=os.path.join(BASE_DIR, "hasil-deteksi"),
    name="jam-lancar",
    conf=0.25
)

print("Deteksi Berhasil") 