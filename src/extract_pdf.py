from pypdf import PdfReader
from pathlib import Path

pdf_dir = Path("/media/sf_Shared_VM/Study/PDFs")

pdf_files = list(pdf_dir.glob("*.pdf"))

if not pdf_files:
    print("No PDF files found.")
    exit()

pdf_path = pdf_files[0]

print(f"Opening: {pdf_path.name}")

reader = PdfReader(pdf_path)

print(f"Pages: {len(reader.pages)}")

for page_num in [0, 1, 2, 5, 10]:
    if page_num >= len(reader.pages):
        continue

    print(f"\n--- PAGE {page_num + 1} ---\n")

    text = reader.pages[page_num].extract_text()

    if text:
        print(text[:1000])
    else:
        print("No text detected")
