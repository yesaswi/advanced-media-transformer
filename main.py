from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from utils import is_valid_storage_path, download_video

app = FastAPI()

class VideoLocationModel(BaseModel):
    path: str


@app.get('/api/process_video')
async def process_video(video_location: VideoLocationModel):
    path = video_location.path

    if not path:
        raise HTTPException(status_code=400, detail="Missing path parameter")
    
    if not is_valid_storage_path(path):
        raise HTTPException(status_code=400, detail="Invalid Path")
    
    # Step 1: Download the video from the given path
    video_file = download_video(path=path)

    if not video_file:
        raise HTTPException(status_code=500, detail="Failed to download video")

    
    return JSONResponse(content={'Path': path, 'Processed': True})


