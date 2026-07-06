import os
import csv
import cv2
from ultralytics import YOLO

# =========================
# LOAD MODEL
# =========================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = YOLO(os.path.join(BASE_DIR, "model/best.pt"))

# =========================
# VIDEO INPUT
# =========================

video_file = "DATASET/jam_lancar.mp4"

video_path = os.path.join(
    BASE_DIR,
    video_file
)

cap = cv2.VideoCapture(video_path)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# =========================
# OUTPUT VIDEO
# =========================

output_dir = os.path.join(
    BASE_DIR,
    "hasil-counting-video"
)

os.makedirs(output_dir, exist_ok=True)

video_name = os.path.splitext(
    os.path.basename(video_file)
)[0]

output_video = os.path.join(
    output_dir,
    f"{video_name}-counting.mp4"
)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

# =========================
# GARIS VIRTUAL
# =========================
line_y = 900

# kendaraan yang sudah dihitung
counted_ids = set()

# counter per kelas
car_count = 0
motorcycle_count = 0
bus_count = 0
truck_count = 0

# =========================
# TRACKING
# =========================

results = model.track(
    source=video_path,
    stream=True,
    persist=True,
    tracker="bytetrack.yaml",
    conf=0.25
)

for result in results:

    frame = result.orig_img

    # gambar garis virtual
    cv2.line(
        frame,
        (500, line_y),
        (3300, line_y),
        (0, 255, 255),
        5
    )

    if result.boxes.id is not None:

        boxes = result.boxes.xyxy.cpu().numpy()
        ids = result.boxes.id.cpu().numpy().astype(int)
        classes = result.boxes.cls.cpu().numpy().astype(int)

        for box, track_id, cls in zip(boxes, ids, classes):

            x1, y1, x2, y2 = map(int, box)

            center_y = (y1 + y2) // 2

            class_name = model.names[cls]

            # gambar bbox
            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                (255, 255, 0),
                2
            )

            label = f"ID:{track_id} {class_name}"

            cv2.putText(
                frame,
                label,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 255),
                2
            )

            # =========================
            # COUNTING
            # =========================

            if center_y > line_y and track_id not in counted_ids:

                counted_ids.add(track_id)

                if class_name == "car":
                    car_count += 1

                elif class_name == "motorcycle":
                    motorcycle_count += 1

                elif class_name == "bus":
                    bus_count += 1

                elif class_name == "truck":
                    truck_count += 1

    # tampilkan counter
    total = (
        car_count +
        motorcycle_count +
        bus_count +
        truck_count
    )

    cv2.putText(
        frame,
        f"Car: {car_count}",
        (50, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.2,
        (0,255,0),
        3
    )

    cv2.putText(
        frame,
        f"Motorcycle: {motorcycle_count}",
        (50, 140),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.2,
        (0,255,0),
        3
    )

    cv2.putText(
        frame,
        f"Bus: {bus_count}",
        (50, 200),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.2,
        (0,255,0),
        3
    )

    cv2.putText(
        frame,
        f"Truck: {truck_count}",
        (50, 260),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.2,
        (0,255,0),
        3
    )

    cv2.putText(
        frame,
        f"Total: {total}",
        (50, 320),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.2,
        (0,0,255),
        3
    )

    out.write(frame)

cap.release()
out.release()

print("\n=== HASIL PENGHITUNGAN ===")
print("Car        :", car_count)
print("Motorcycle :", motorcycle_count)
print("Bus        :", bus_count)
print("Truck      :", truck_count)
print("Total      :", total)

print("\nVideo tersimpan di:")
print(output_video)

# =========================
# SIMPAN KE CSV
# =========================

csv_file = os.path.join(
    output_dir,
    f"{video_name}.csv"
)

with open(csv_file, mode="w", newline="") as file:

    writer = csv.writer(
        file,
        delimiter=";"
    )

    writer.writerow(["Jenis Kendaraan", "Jumlah"])

    writer.writerow(["Car", car_count])
    writer.writerow(["Motorcycle", motorcycle_count])
    writer.writerow(["Bus", bus_count])
    writer.writerow(["Truck", truck_count])
    writer.writerow(["Total", total])

print("\nCSV tersimpan di:")
print(csv_file)