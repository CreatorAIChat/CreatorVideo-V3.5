from dataclasses import dataclass
import torch
@dataclass
class CharacterState:
    character_id:str
    appearance:torch.Tensor|None=None
    face:torch.Tensor|None=None
    clothing:torch.Tensor|None=None
class CharacterMemory:
    def __init__(self,max_slots=32): self.max_slots=max_slots; self.items={}
    def upsert(self,state):
        if len(self.items)>=self.max_slots and state.character_id not in self.items: self.items.pop(next(iter(self.items)))
        self.items[state.character_id]=state
    def get(self,k): return self.items.get(k)
