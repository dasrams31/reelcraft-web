import os
import hashlib

SRT_CACHE_DIR = "/tmp/reelcraft_audio"
os.makedirs(SRT_CACHE_DIR, exist_ok=True)

def parse_time_str(time_str: str):
    # e.g. "00:00 - 00:04" or "00:08 - 00:20"
    try:
        parts = time_str.split("-")
        start = parts[0].strip()
        end = parts[1].strip()
        
        start_min, start_sec = map(int, start.split(":"))
        end_min, end_sec = map(int, end.split(":"))
        
        start_fmt = f"00:{start_min:02d}:{start_sec:02d},000"
        end_fmt = f"00:{end_min:02d}:{end_sec:02d},000"
        return start_fmt, end_fmt
    except:
        return "00:00:00,000", "00:00:05,000"

def generate_srt_content(scenes: list) -> str:
    srt_lines = []
    for idx, scene in enumerate(scenes, 1):
        start_t, end_t = parse_time_str(scene.get("time", "00:00 - 00:05"))
        text = scene.get("voiceover", "")
        
        srt_lines.append(f"{idx}")
        srt_lines.append(f"{start_t} --> {end_t}")
        srt_lines.append(f"{text}\n")
        
    return "\n".join(srt_lines)

def save_srt_file(scenes: list, prefix: str = "subtitles") -> str:
    content = generate_srt_content(scenes)
    text_hash = hashlib.md5(content.encode('utf-8')).hexdigest()[:12]
    filename = f"{prefix}_{text_hash}.srt"
    filepath = os.path.join(SRT_CACHE_DIR, filename)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
        
    return filename
