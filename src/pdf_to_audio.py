from pypdf import PdfReader
from pathlib import Path
import subprocess

pdf_dir = Path("/media/sf_Shared_VM/Study/PDFs")

pdf_files = list(pdf_dir.glob("*.pdf"))

if not pdf_files:
    print("No PDF found")
    exit()

pdf_path = pdf_files[0]

print(f"Opening: {pdf_path.name}")

reader = PdfReader(pdf_path)

# Extract first 3 pages of actual content
text = ""

for page_num in range(1, 4):
    page_text = reader.pages[page_num].extract_text()

    if page_text:
        text += page_text + "\n"

# Save extracted text
with open("output/book_text.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("Text saved")

# Generate audio
subprocess.run(
    [
        "./piper/piper",
        "--model",
        "voices/en_US-lessac-medium.onnx",
        "--output_file",
        "output/linux_book_sample.wav",
    ],
    input=text,
    text=True,
)

print("Audio generated")
