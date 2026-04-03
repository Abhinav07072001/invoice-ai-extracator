import google.generativeai as genai
import json
import os

# configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def parse_invoice(text):

    prompt = f"""
Extract structured invoice data from this text.

Return ONLY valid JSON with the following fields:
vendor
invoice_number
date
total
tax
currency

Text:
{text}
"""

    try:
        # Use a stable model supported by the API
        model = genai.GenerativeModel("gemini-1.0-pro")

        response = model.generate_content(prompt)

        result_text = response.text

        # Try converting AI output to JSON
        try:
            parsed = json.loads(result_text)
            return parsed
        except:
            return {"raw_ai_response": result_text}

    except Exception as e:
        return {"error": str(e)}