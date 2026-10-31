# Real-Time Face Analysis (Gender, Age, Race, Emotion)

Proyek ini adalah aplikasi deteksi dan analisis wajah secara *real-time* menggunakan webcam. Aplikasi ini memanfaatkan **DeepFace** dan **OpenCV** untuk mendeteksi wajah serta memprediksi gender, usia, ras, dan emosi dominan.

## Fitur
- Deteksi wajah secara *real-time* melalui webcam.
- Analisis 4 atribut sekaligus: Gender, Usia, Ras, dan Emosi.
- Visualisasi *bounding box* dan label informasi pada frame video.
- Optimasi pemrosesan (setiap 15 frame) untuk mencegah *lag* pada video.

## Persyaratan
- Python 3.8 - 3.11
- Webcam (Internal atau Eksternal)
- Koneksi internet (untuk mengunduh model DeepFace pada pertama kali dijalankan)

## Instalasi

1. Clone atau unduh repositori ini.
2. Buat dan aktifkan *virtual environment* (disarankan):
   ```bash
   python -m venv env
   # Windows
   env\Scripts\activate
   # Linux/Mac
   source env/bin/activate
   ```
3. Instal *dependencies* yang dibutuhkan:
   ```bash
   pip install -r requirements.txt
   ```

## Cara Menjalankan

Jalankan script utama dengan perintah:
```bash
python gender_age_race_emotion_detector.py
```
- Tekan tombol **`q`** pada jendela video untuk keluar dari aplikasi.

## Troubleshooting
- **Webcam tidak terdeteksi / Layar hitam:** 
  Buka file `gender_age_race_emotion_detector.py`, lalu ubah indeks pada `cv2.VideoCapture(1)` menjadi `0` atau `2` tergantung pada indeks kamera di perangkat Anda.
  *(Catatan: Pastikan baris komentar `Ganti 0 ke 1...` di dalam script diawali dengan tanda `#` agar tidak terjadi SyntaxError).*
- **Aplikasi terasa lambat / Lag:**
  Aplikasi sudah diatur untuk memproses analisis setiap 15 frame. Jika masih lambat, Anda bisa menaikkan angka tersebut (misal: `frame_count % 30 == 0`) di dalam script.