from dataclasses import dataclass
@dataclass
class SceneState:
    scene_id:str
    description:str=""
    embedding:object=None
class SceneMemory:
    def __init__(self,max_slots=32): self.max_slots=max_slots; self.items={}
    def put(self,state):
        if len(self.items)>=self.max_slots and state.scene_id not in self.items: self.items.pop(next(iter(self.items)))
        self.items[state.scene_id]=state
    def get(self,k): return self.items.get(k)
