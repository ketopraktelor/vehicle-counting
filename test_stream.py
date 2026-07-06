# import cv2

# url = "https://dishub.depok.go.id/vi/10109059.m3u8"

# cap = cv2.VideoCapture(url, cv2.CAP_FFMPEG)


# if not cap.isOpened():
#     print("Gagal membuka stream")
#     exit()

# fps = cap.get(cv2.CAP_PROP_FPS)
# print("FPS:", fps)

# while True:
#     ret, frame = cap.read()

#     if not ret:
#         print("Frame gagal dibaca")
#         break

#     cv2.imshow("CCTV", frame)
    
#     delay = int(1000 / fps)  # Delay dalam milidetik

#     if cv2.waitKey(delay) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

# import cv2

# url = "https://dishub.depok.go.id/vi/10109059.m3u8"

# cap = cv2.VideoCapture(url, cv2.CAP_FFMPEG)

# print("FPS :", cap.get(cv2.CAP_PROP_FPS))
# print("Frame Count :", cap.get(cv2.CAP_PROP_FRAME_COUNT))

# import cv2
# import time

# url = "https://dishub.depok.go.id/vi/10109059.m3u8"

# cap = cv2.VideoCapture(url, cv2.CAP_FFMPEG)

# fps = cap.get(cv2.CAP_PROP_FPS)
# print("FPS:", fps)

# while True:
#     start = time.time()

#     ret, frame = cap.read()

#     if not ret:
#         print("Frame gagal")
#         break

#     cv2.imshow("CCTV", frame)

#     elapsed = time.time() - start
#     print(f"Read frame: {elapsed:.4f} detik")

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

# import cv2
# import time

# url = "https://dishub.depok.go.id/vi/10109059.m3u8"

# ==========================================
# Fungsi untuk membuka koneksi CCTV
# ==========================================
# def connect():
#     print("Menghubungkan ke CCTV...")

#     cap = cv2.VideoCapture(url, cv2.CAP_FFMPEG)

#     if not cap.isOpened():
#         print("Gagal membuka stream")
#         return None

#     # Buffer kecil supaya tidak delay
#     cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

#     fps = cap.get(cv2.CAP_PROP_FPS)

#     if fps <= 0:
#         fps = 15

#     print(f"Berhasil terhubung | FPS = {fps}")

#     return cap, fps


# ==========================================
# Koneksi pertama
# ==========================================
# result = connect()

# if result is None:
#     exit()

# cap, fps = result

# delay = int(1000 / fps)


# ==========================================
# Loop utama
# ==========================================
# while True:

#     ret, frame = cap.read()

#     # Jika stream putus
#     if not ret:

#         print("\nStream terputus...")
#         cap.release()

#         time.sleep(2)

#         result = connect()

#         if result is None:
#             print("Reconnect gagal.")
#             break

#         cap, fps = result
#         delay = int(1000 / fps)

#         continue

#     cv2.imshow("CCTV", frame)

#     key = cv2.waitKey(delay)

#     if key & 0xFF == ord('q'):
#         break


# cap.release()
# cv2.destroyAllWindows()