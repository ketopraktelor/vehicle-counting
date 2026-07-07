import subprocess
import os

print("=" * 60)
print("            CCTV VIDEO FEED RECORDER")
print("=" * 60)

url = input("URL M3U8              : ").strip()

if url == "":
    print("URL tidak boleh kosong.")
    exit()

filename = input("Nama file (tanpa .mp4): ").strip()

if filename == "":
    filename = "record"

folder = input("Folder penyimpanan (Enter = DATASET): ").strip()

if folder == "":
    folder = r"C:\Rekaman CCTV"

os.makedirs(folder, exist_ok=True)

try:
    menit = int(input("Durasi rekaman (menit): "))
except ValueError:
    print("Durasi tidak valid.")
    exit()

output_file = os.path.join(folder, filename + ".mp4")

print("\n")
print("=" * 60)
print("Mulai merekam...")
print("=" * 60)
print("Output :", output_file)
print("Durasi :", menit, "menit")
print("=" * 60)
print()

cmd = [

    "ffmpeg",

    "-hide_banner",

    "-loglevel", "warning",

    # reconnect otomatis
    "-reconnect", "1",
    "-reconnect_streamed", "1",
    "-reconnect_at_eof", "1",
    "-reconnect_delay_max", "5",

    "-rw_timeout", "15000000",

    "-i", url,

    "-t", str(menit * 60),

    # Encode ulang supaya MP4 valid
    "-c:v", "libx264",
    "-preset", "veryfast",
    "-crf", "23",

    "-c:a", "aac",

    "-movflags", "+faststart",

    "-y",

    output_file

]

try:

    subprocess.run(cmd)

except KeyboardInterrupt:

    print("\nRekaman dihentikan.")

print("\n")

if os.path.exists(output_file):

    size = os.path.getsize(output_file) / (1024 * 1024)

    print("=" * 60)
    print("REKAMAN SELESAI")
    print("=" * 60)
    print("Lokasi :", os.path.abspath(output_file))
    print(f"Ukuran : {size:.2f} MB")
    print("=" * 60)

else:

    print("Rekaman gagal.")