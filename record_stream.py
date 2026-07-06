import subprocess
import os
from pathlib import Path

# ==========================================================
# KONFIGURASI
# ==========================================================

STREAM_URL = "https://dishub.depok.go.id/vi/10109059.m3u8"

OUTPUT_FOLDER = "DATASET"

# ==========================================================

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

print("=" * 55)
print("         CCTV VIDEO FEED RECORDER")
print("=" * 55)
print("1. Rekam Jam Sibuk")
print("2. Rekam Jam Lancar")
print("3. Custom")
print("=" * 55)

pilihan = input("Pilih menu (1/2/3): ").strip()

if pilihan == "1":
    filename = "jam_sibuk.mp4"

elif pilihan == "2":
    filename = "jam_lancar.mp4"

elif pilihan == "3":

    nama = input("Masukkan nama file : ").strip()

    if not nama:
        nama = "record"

    if not nama.endswith(".mp4"):
        nama += ".mp4"

    filename = nama

else:
    print("Pilihan tidak valid.")
    exit()

# ==========================================================

try:
    menit = int(input("Durasi rekaman (menit): "))
except:
    print("Input durasi tidak valid.")
    exit()

durasi = menit * 60

output_path = os.path.join(OUTPUT_FOLDER, filename)

print("\n" + "=" * 55)
print("Memulai proses rekaman...")
print("=" * 55)
print(f"Source  : {STREAM_URL}")
print(f"Output  : {output_path}")
print(f"Durasi  : {menit} menit")
print("=" * 55)
print("\nTekan CTRL + C jika ingin menghentikan rekaman lebih awal.\n")

# ==========================================================
# COMMAND FFMPEG
# ==========================================================

cmd = [
    "ffmpeg",

    # Tampilan log
    "-hide_banner",
    "-loglevel", "info",

    # ===========================
    # AUTO RECONNECT
    # ===========================
    "-reconnect", "1",
    "-reconnect_streamed", "1",
    "-reconnect_at_eof", "1",
    "-reconnect_on_network_error", "1",
    "-reconnect_on_http_error", "4xx,5xx",
    "-reconnect_delay_max", "5",

    "-rw_timeout", "15000000",

    # Input CCTV
    "-i", STREAM_URL,
    "-t", str(durasi),
    "-c", "copy",
    "-y",

    output_path
]

try:

    subprocess.run(cmd)

except KeyboardInterrupt:

    print("\n\nRekaman dihentikan oleh pengguna.")

# ==========================================================
# HASIL
# ==========================================================

print("\n" + "=" * 55)

if os.path.exists(output_path):

    ukuran = os.path.getsize(output_path) / (1024 * 1024)

    print("Rekaman berhasil disimpan.")
    print(f"Lokasi File : {Path(output_path).resolve()}")
    print(f"Ukuran File : {ukuran:.2f} MB")

else:

    print("Rekaman gagal.")

print("=" * 55)