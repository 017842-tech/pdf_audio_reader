from pathlib import Path
import re

# Input and output folders
text_dir = Path("/media/sf_Shared_VM/Study/Text")
output_dir = Path("/media/sf_Shared_VM/Study/Text/Cleaned")

output_dir.mkdir(parents=True, exist_ok=True)

# Find all txt files
txt_files = list(text_dir.glob("*.txt"))

if not txt_files:
    print("No text files found.")
    exit()

for txt_file in txt_files:

    print(f"Processing: {txt_file.name}")

    with open(txt_file, "r", encoding="utf-8") as f:
        text = f.read()

    # Remove standalone page numbers
    text = re.sub(r"^\s*\d+\s*$", "", text, flags=re.MULTILINE)

    # Remove repeated book title/header
    text = re.sub(r"How Linux Works.*", "", text)

    # Remove excessive blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Remove extra spaces
    text = re.sub(r"[ \t]+", " ", text)

    # Remove leading/trailing whitespace
    text = text.strip()

    output_file = output_dir / f"{txt_file.stem}_cleaned.txt"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"Saved: {output_file}")

print("\nText cleaning complete.")
