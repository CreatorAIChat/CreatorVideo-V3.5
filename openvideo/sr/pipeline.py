class VideoSRPipeline:
    def upscale(self,input_path,target_resolution,output_path):
        return {"input":input_path,"output":output_path,"target":target_resolution,"status":"adapter_not_loaded"}
