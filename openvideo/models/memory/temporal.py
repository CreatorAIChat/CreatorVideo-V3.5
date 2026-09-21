class TemporalMemory:
    def __init__(self,max_history=8): self.max_history=max_history; self.latents=[]
    def push(self,x): self.latents=(self.latents+[x])[-self.max_history:]
    def context(self): return self.latents
