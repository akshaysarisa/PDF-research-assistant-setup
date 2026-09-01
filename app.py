import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
api_key=os.getenv("GEMINI_API_KEY")
)

pdf=client.files.upload(
    file="Book_PDF_Guidelines for Priests7.pdf"
)
response=client.models.generate_content(
    model="gemini-3.6-flash",
    contents=[
        pdf,
        "What is this document about? give me a simple summary"
              ]
)
print(response.text)