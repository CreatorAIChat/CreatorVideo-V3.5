import math
from dataclasses import dataclass,asdict
@dataclass
class Shot:
    index:int
    start:float
    end:float
    prompt:str
    camera:str="CINEMATIC"
def plan(prompt,duration,shot_seconds=8):
    n=max(1,math.ceil(duration/shot_seconds))
    return [asdict(Shot(i+1,i*shot_seconds,min(duration,(i+1)*shot_seconds),prompt)) for i in range(n)]
