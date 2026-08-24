from pypdf import PdfReader
reader=PdfReader("Book_PDF_Guidelines for Priests7.pdf")
print("number of pages:",len(reader.pages))
for page_number, page in enumerate(reader.pages,start=1):
    text=page.extract_text()
    print("PAGE",page_number)
    print("Characters extracted:",len(text or ""))
    print(repr(text[:200] if text else "NO TEXT"))
    print("-" * 50)
    