import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
api_key=os.getenv("GEMINI_API_KEY")
)
pdf = client.files.upload(
    file="Book_PDF_Guidelines for Priests7.pdf"
)

chat = client.chats.create(
    model="gemini-3.6-flash"
)
# First: make Gemini read the PDF and summarize it

response = chat.send_message(
    [
        pdf,
        "Read and understand this PDF. and give me a simple summary ."
    ]
)

print("\nPDF SUMMARY:")
print(response.text)

print("\nPDF loaded successfully.")
print("Ask questions about the PDF")
print("Type 'exit' to quit\n")
#Q&A mode
while True:
    question = input("You: ")
    if question.lower() == "exit":
        break
    response= chat.send_message(question)

    print("PDF Assistant: ", response.text)