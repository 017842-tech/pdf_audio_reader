from pypdf import PdfReader
from pathlib import Path

pdf_dir = Path("/media/sf_Shared_VM/Study/PDFs")
text_dir = Path("/media/sf_Shared_VM/Study/Text")

text_dir.mkdir(exist_ok=True)

pdf_files = list(pdf_dir.glob("*.pdf"))

if not pdf_files:
    print("No PDF found")
    exit()

pdf_path = pdf_files[0]

reader = PdfReader(pdf_path)

all_text = ""

for page in reader.pages:
    text = page.extract_text()

    if text:
        all_text += text + "\n\n"

output_file = text_dir / f"{pdf_path.stem}.txt"

with open(output_file, "w", encoding="utf-8") as f:
    f.write(all_text)

print(f"Saved: {output_file}")
