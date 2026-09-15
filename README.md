# 🎬 ReelCraft Web Engine

**ReelCraft** adalah platform otomasi pembuatan video pendek/reels, perancangan naskah bertenaga AI, pembuatan voiceover otomatis (TTS), generator subtitle (SRT), dan rendering video dinamis.

Dibuat oleh: **Rama Danadipa (@dasrams / Rama D)**  
URL Layanan: **https://reelcraft.dasrams.biz.id**

---

## 🌟 Fitur Utama

- **AI Script Generator:** Pembuatan naskah cerita dan hook video pendek otomatis berbasis AI.
- **Voiceover Synthesis:** Engine konversi naskah ke narasi audio suara jernih.
- **Auto SRT Subtitle Generator:** Sinkronisasi teks caption otomatis per timestamp.
- **Web Interface:** Tampilan dashboard web responsif untuk preview dan kontrol render video.
- **FastAPI Backend:** Engine async berkecepatan tinggi dengan integrasi microservices.

---

## 🚀 Struktur Direktori

```text
├── app.py                  # Entry point FastAPI & REST endpoints
├── engine/
│   ├── script_engine.py    # Modul pembuat skrip naskah AI
│   ├── voice_engine.py     # Modul generator audio / TTS
│   └── srt_engine.py       # Modul kalkulasi timestamp & file subtitle SRT
├── static/
│   ├── index.html          # Web UI interface
│   ├── style.css           # Styling & layout
│   └── app.js              # Client-side interaction & rendering preview
├── .gitignore
└── README.md
```

---

## 🛠️ Cara Menjalankan Secara Lokal / VPS

1. **Siapkan Virtual Environment & Install Dependencies:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install fastapi uvicorn pydantic requests
   ```

2. **Jalankan Server:**
   ```bash
   python3 -m uvicorn app:app --host 0.0.0.0 --port 8080 --reload
   ```

3. **Akses di Browser:**
   Buka `http://localhost:8080` atau `https://reelcraft.dasrams.biz.id`

---
*© 2026 Rama Danadipa (DasRams) · All rights reserved.*
