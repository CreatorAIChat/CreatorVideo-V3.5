from pathlib import Path
class MockBackend:
    def __init__(self,root="storage"): self.root=Path(root); self.root.mkdir(exist_ok=True)
    def generate(self,shot,resolution):
        p=self.root/f"shot_{shot['index']:04d}.txt"
        p.write_text(f"MOCK VIDEO SHOT\n{shot}\nresolution={resolution}\n",encoding="utf-8")
        return {"path":str(p),"status":"mock"}
