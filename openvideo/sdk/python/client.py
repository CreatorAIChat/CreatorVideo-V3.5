import requests
class VideoClient:
    def __init__(self,base_url="http://127.0.0.1:8000",api_key=None):
        self.base_url=base_url.rstrip("/"); self.headers={"Authorization":f"Bearer {api_key}"} if api_key else {}
    def generate(self,**kwargs):
        r=requests.post(self.base_url+"/v1/videos",json=kwargs,headers=self.headers); r.raise_for_status(); return r.json()
    def get(self,task_id):
        r=requests.get(self.base_url+f"/v1/videos/{task_id}",headers=self.headers); r.raise_for_status(); return r.json()
