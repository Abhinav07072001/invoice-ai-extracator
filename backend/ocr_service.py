import pytesseract
from PIL import Image
import platform

# Only set path for Windows (local development)
if platform.system() == "Windows":
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text(file_path):
    try:
        image = Image.open(file_path)

        # try OCR
        text = pytesseract.image_to_string(image)

        if not text.strip():
            return "No text detected in image"

        return text

    except Exception as e:
        # Handle cases where tesseract is not installed on server
        return f"OCR error: {str(e)}"