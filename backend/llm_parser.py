from google import genai
import json

# create Gemini client
client = genai.Client(api_key="AIzaSyCa8IIalyUh-OQFwVdyFldj-Uf6PyHgozU")


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
        response = client.models.generate_content(
            model="gemini-1.5-flash-latest",
            contents=prompt
        )

        result_text = response.text

        # Try converting AI output to JSON
        try:
            parsed = json.loads(result_text)
            return parsed
        except:
            return {"raw_ai_response": result_text}

    except Exception as e:
        return {"error": str(e)}