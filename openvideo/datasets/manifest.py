from pathlib import Path
import json
EXT={".mp4",".mov",".webm",".mkv"}
def build(root): return [{"video":str(p)} for p in Path(root).rglob("*") if p.suffix.lower() in EXT]
if __name__=="__main__":
    import argparse
    p=argparse.ArgumentParser();p.add_argument("root");p.add_argument("--out",default="manifest.json");a=p.parse_args()
    Path(a.out).write_text(json.dumps(build(a.root),indent=2),encoding="utf-8")
