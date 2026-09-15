import os
import sys
from typing import Optional
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

from engine.script_engine import generate_storyboard, DESTINATION_KNOWLEDGE
from engine.voice_engine import generate_voice_audio, AUDIO_CACHE_DIR
from engine.srt_engine import save_srt_file

app = FastAPI(
    title="ReelCraft AI - Mountain & Travel Video Story Studio",
    version="1.0.0"
)

# Mount static files
static_dir = os.path.join(BASE_DIR, "static")
os.makedirs(static_dir, exist_ok=True)
app.mount("/static", StaticFiles(directory=static_dir), name="static")

class GenerateRequest(BaseModel):
    destination: str
    duration: int = 30
    tone: str = "cinematic"
    voice: str = "id_ardi"

@app.get("/", response_class=HTMLResponse)
async def read_index():
    index_file = os.path.join(static_dir, "index.html")
    if os.path.exists(index_file):
        with open(index_file, "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>ReelCraft AI Studio is running!</h1>"

@app.get("/api/destinations")
def get_destinations():
    dest_list = []
    for k, v in DESTINATION_KNOWLEDGE.items():
        dest_list.append({
            "key": k,
            "title": v["title"],
            "elev": v["elev"],
            "fact": v["fact"]
        })
    return {"destinations": dest_list}

@app.post("/api/generate")
async def generate_content(req: GenerateRequest):
    if not req.destination or len(req.destination.strip()) < 2:
        raise HTTPException(status_code=400, detail="Nama destinasi tidak boleh kosong.")
        
    # 1. Generate script & storyboard
    storyboard = generate_storyboard(
        destination=req.destination,
        duration_sec=req.duration,
        tone=req.tone
    )
    
    # 2. Generate Voiceover Audio (MP3)
    audio_filename = await generate_voice_audio(
        text=storyboard["full_voiceover"],
        voice_key=req.voice
    )
    
    # 3. Generate SRT Subtitles
    srt_filename = save_srt_file(
        scenes=storyboard["scenes"],
        prefix=f"sub_{req.destination.lower()[:8]}"
    )
    
    return {
        "success": True,
        "storyboard": storyboard,
        "audio_url": f"/api/audio/{audio_filename}",
        "audio_filename": audio_filename,
        "srt_url": f"/api/download/srt/{srt_filename}",
        "srt_filename": srt_filename
    }

@app.get("/api/audio/{filename}")
def get_audio(filename: str):
    file_path = os.path.join(AUDIO_CACHE_DIR, filename)
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="audio/mpeg", filename=filename)
    raise HTTPException(status_code=404, detail="Audio file not found")

@app.get("/api/download/{file_type}/{filename}")
def download_file(file_type: str, filename: str):
    file_path = os.path.join(AUDIO_CACHE_DIR, filename)
    if os.path.exists(file_path):
        media_type = "application/x-subrip" if file_type == "srt" else "audio/mpeg"
        return FileResponse(file_path, media_type=media_type, filename=filename)
    raise HTTPException(status_code=404, detail="File not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
