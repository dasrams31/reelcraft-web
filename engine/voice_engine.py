import os
import asyncio
import edge_tts
import hashlib

AUDIO_CACHE_DIR = "/tmp/reelcraft_audio"
os.makedirs(AUDIO_CACHE_DIR, exist_ok=True)

VOICES = {
    "id_ardi": "id-ID-ArdiNeural",     # Pria, Berat & Naratif
    "id_gadis": "id-ID-GadisNeural",   # Wanita, Jernih & Dinamis
    "en_christopher": "en-US-ChristopherNeural", # English Male
    "en_jenny": "en-US-JennyNeural"    # English Female
}

async def generate_voice_audio(text: str, voice_key: str = "id_ardi") -> str:
    voice_name = VOICES.get(voice_key, "id-ID-ArdiNeural")
    
    # Generate unique hash filename based on text and voice
    text_hash = hashlib.md5(f"{text}_{voice_name}".encode('utf-8')).hexdigest()[:12]
    filename = f"vo_{text_hash}.mp3"
    filepath = os.path.join(AUDIO_CACHE_DIR, filename)
    
    if os.path.exists(filepath) and os.path.getsize(filepath) > 1000:
        return filename
        
    communicate = edge_tts.Communicate(text, voice_name, rate="+0%", pitch="+0Hz")
    await communicate.save(filepath)
    return filename

def generate_voice_sync(text: str, voice_key: str = "id_ardi") -> str:
    return asyncio.run(generate_voice_audio(text, voice_key))
