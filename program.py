import cv2
from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import HTMLResponse
from multiprocessing import Process
import uvicorn
import base64

app = FastAPI()

class VideoProcessor:
    def __init__(self, rtsp_url):
        self.rtsp_url = rtsp_url
        self.frames = []

    def read_frames(self):
        self.capture = cv2.VideoCapture(self.rtsp_url)
        while True:
            ret, frame = self.capture.read()
            if not ret:
                break
            self.frames.append(frame)

    def stop_reading(self):
        self.capture.release()

    def get_brightest_frames(self, num_frames=9):
        print(len(self.frames))
        brightest_frames = sorted(self.frames, key=lambda frame: cv2.mean(frame), reverse=True)[:num_frames]
        return brightest_frames

video_processor = None
video_read_process=None

@app.post("/start")
async def start(rtsp_url: str):
    global video_processor
    global video_read_process
    if video_processor:
        raise HTTPException(status_code=400, detail="Video processing already started.")
    
    video_processor = VideoProcessor(rtsp_url)
    video_read_process = Process(target=video_processor.read_frames)
    video_read_process.start()
    

    return {"message": "Video processing started."}

@app.post("/stop", response_class=HTMLResponse)
async def stop():
    global video_processor
    if not video_processor:
        raise HTTPException(status_code=400, detail="No video processing in progress.")
    
    #video_processor.stop_reading()

    video_read_process.terminate()
    brightest_frames = video_processor.get_brightest_frames()

    # Create a 3x3 grid of the brightest frames
    grid_image = cv2.vconcat([cv2.hconcat(brightest_frames[i:i+3]) for i in range(0, 9, 3)])

    # Resize the image to 900x900
    resized_image = cv2.resize(grid_image, (900, 900))

    # Save the image
    cv2.imwrite("brightest_frames.jpg", resized_image)

    # Clear the frames
    video_processor.frames = []
    video_processor = None

    # Display the image in the HTML response
    with open("brightest_frames.jpg", "rb") as img_file:
        image_content = img_file.read()

    return HTMLResponse(content=f"<img src='data:image/jpeg;base64,{base64.b64encode(image_content).decode()}'>")

if __name__ == "__main__":
    
    uvicorn.run(app, host="127.0.0.1", port=8000)
