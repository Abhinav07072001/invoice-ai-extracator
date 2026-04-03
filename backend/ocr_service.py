import pytesseract
from PIL import Image

# tell python where tesseract is installed
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text(file_path):
    image = Image.open(file_path)
    text = pytesseract.image_to_string(image)
    return text