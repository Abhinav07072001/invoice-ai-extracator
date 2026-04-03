import pytesseract
from PIL import Image
import os
import platform

# Only set path for Windows (local development)
if platform.system() == "Windows":
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text(file_path):
    try:
        image = Image.open(file_path)

        text = pytesseract.image_to_string(image)

        return text

    except Exception as e:
        return str(e)