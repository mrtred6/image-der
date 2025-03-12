from fastapi import FastAPI
from PIL import Image, ImageDraw
from io import BytesIO
import base64

app = FastAPI()

def create_image(text):
    img = Image.new("RGB", (300, 100), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.text((10, 40), text, fill=(0, 0, 0))
    
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    
    return base64.b64encode(buffer.getvalue()).decode()

@app.get("/")
def home():
    return {"message": "Image Generator API is running!"}

@app.get("/generate/")
def generate_image(text: str):
    image_base64 = create_image(text)
    return {"image": image_base64}
