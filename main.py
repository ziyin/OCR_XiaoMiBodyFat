from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import easyocr
import numpy as np
import cv2
import re

app = FastAPI()

reader = easyocr.Reader(['ch_tra', 'en'], gpu=False)

@app.post("/predict-xiao-mi-body-fat")
async def predict_body_fat(file: UploadFile = File(...)):
    contents = await file.read()
    npimg = np.frombuffer(contents, np.uint8)
    image = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    results = reader.readtext(image)
    texts = [text for (_, text, _) in results]
    combined_text = " ".join(texts)
    match = re.search(r'(?:體脂肪率|體脂肪|Body Fat)[^\d]*(\d{2,3}\.\d)', combined_text)
    if not match:
        match = re.search(r'(\d{2,3}\.\d)\s*%', combined_text)

    body_fat = match.group(1) if match else None
    return JSONResponse(content={
        "success": body_fat is not None,
        "body_fat": body_fat
    })