import cv2
from deepface import DeepFace

# Ganti 0 ke 1 atau 2 jika webcam portable tidak terdeteksi
cap = cv2.VideoCapture(1) 
frame_count = 0
last_data = {"emotion": "Scanning...", "age": "...", "race": "...", "gender": "...", "region": None}

print("Memuat model...")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1
    
    # Proses deteksi setiap 15 frame agar video tidak lag
    if frame_count % 15 == 0:
        try:
            # Tambahkan 'gender' di actions
            results = DeepFace.analyze(frame, actions=['emotion', 'age', 'race', 'gender'], enforce_detection=False)
            
            if isinstance(results, list) and len(results) > 0:
                res = results[0]
                last_data['emotion'] = res.get('dominant_emotion', 'Unknown')
                last_data['age'] = int(res.get('age', 0))
                last_data['race'] = res.get('dominant_race', 'Unknown')
                last_data['gender'] = res.get('dominant_gender', 'Unknown')
                
                r = res.get('region', {})
                if r:
                    last_data['region'] = (r['x'], r['y'], r['w'], r['h'])
        except Exception:
            pass

    # Gambar kotak dan teks
    if last_data['region']:
        x, y, w, h = last_data['region']
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        # Gabungkan semua data
        text = f"{last_data['gender']} | {last_data['age']} | {last_data['race'].capitalize()} | {last_data['emotion']}"
        cv2.putText(frame, text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow('Deteksi Wajah Lengkap - Tekan Q', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()