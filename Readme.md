## Purpose

Extract the body fat percentage from the test results of the Xiaomi Body Fat Scale.

## Approach

Use EasyOCR to read text from the image, and extract the body fat information using regular expressions.

## Installation

Please install the required packages:

```bash
pip install fastapi uvicorn easyocr opencv-python
```