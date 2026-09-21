from .planner import plan
class LongVideoGenerator:
    def __init__(self,backend=None): self.backend=backend
    def generate(self,prompt,duration,resolution="1080p",shot_seconds=8):
        shots=plan(prompt,duration,shot_seconds)
        outputs=[self.backend.generate(s,resolution) if self.backend else {"shot":s,"status":"planned"} for s in shots]
        return {"duration":duration,"resolution":resolution,"shots":outputs,"status":"planned"}
