from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from rembg import remove
from PIL import Image
import io

app = FastAPI()

@app.post("/remove-bg")
async def remove_background(file: UploadFile = File(...)):
    input_image = Image.open(file.file)
    output_image = remove(input_image)
    
    img_io = io.BytesIO()
    output_image.save(img_io, "PNG")
    img_io.seek(0)
    
    return StreamingResponse(img_io, media_type="image/png")

@app.get("/")
def health():
    return {"status": "BG Remover API running ✅"}
