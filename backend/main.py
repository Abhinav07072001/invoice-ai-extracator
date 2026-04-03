from fastapi import FastAPI, UploadFile, File
from ocr_service import extract_text
from llm_parser import parse_invoice
from supabase_client import supabase
import shutil
import os

app = FastAPI()

UPLOAD_FOLDER = "uploads"

# create upload folder if not exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.get("/")
def home():
    return {"message": "Invoice AI Backend Running 🚀"}


@app.post("/upload")
async def upload_invoice(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "filename": file.filename,
        "message": "File uploaded successfully"
    }


@app.post("/process")
async def process_invoice(file: UploadFile = File(...)):

    try:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)

        # save file
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # OCR extraction
        text = extract_text(file_path)

        # AI parsing
        parsed_data = parse_invoice(text)

        # save into supabase
        if isinstance(parsed_data, dict) and "vendor" in parsed_data:

            supabase.table("invoices").insert({
                "vendor": parsed_data.get("vendor"),
                "invoice_number": parsed_data.get("invoice_number"),
                "date": parsed_data.get("date"),
                "total": parsed_data.get("total"),
                "tax": parsed_data.get("tax"),
                "currency": parsed_data.get("currency")
            }).execute()

        return {
            "ocr_text": text,
            "ai_parsed": parsed_data
        }

    except Exception as e:
        return {
            "error": str(e)
        }