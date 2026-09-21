from fastapi import FastAPI,BackgroundTasks
from pydantic import BaseModel,Field
from uuid import uuid4
from openvideo.long_video.generator import LongVideoGenerator
from openvideo.inference.mock_backend import MockBackend
from openvideo.long_video.planner import plan

app=FastAPI(title="CreatorVideo API",version="6.0.0")
tasks={}
generator=LongVideoGenerator(MockBackend())

class GenerateRequest(BaseModel):
    prompt:str=Field(min_length=1)
    duration:int=Field(default=8,ge=1,le=3600)
    resolution:str=Field(default="1080p",pattern="^(720p|1080p|2k|4k)$")
    fps:int=Field(default=24,ge=1,le=120)
    aspect_ratio:str="16:9"

def worker(tid,req):
    tasks[tid]["status"]="generating"
    result=generator.generate(req.prompt,req.duration,req.resolution)
    tasks[tid].update(status="completed",progress=100,result=result)

@app.get("/")
def root(): return {"name":"CreatorVideo","version":"6.0.0","status":"ok"}

@app.get("/v1/models")
def models(): return {"data":[{"id":"creatorvideo-v3-5","type":"video-generation","status":"research"}]}

@app.post("/v1/videos")
def create(req:GenerateRequest,bg:BackgroundTasks):
    tid="ov_"+uuid4().hex[:12]
    tasks[tid]={"id":tid,"status":"queued","progress":0,"duration":req.duration,"resolution":req.resolution}
    bg.add_task(worker,tid,req)
    return tasks[tid]

@app.get("/v1/videos/{tid}")
def get_task(tid:str): return tasks.get(tid,{"error":"task_not_found"})

@app.get("/v1/video/plan")
def make_plan(prompt:str,duration:int=120): return {"plan":plan(prompt,duration)}
