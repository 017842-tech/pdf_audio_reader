from pathlib import Path
import re

# Source cleaned text
input_dir = Path("/media/sf_Shared_VM/Study/Text/Cleaned")

# Output chapters
output_dir = Path("/media/sf_Shared_VM/Study/Text/Chapters")
output_dir.mkdir(parents=True, exist_ok=True)

txt_files = list(input_dir.glob("*_cleaned.txt"))

if not txt_files:
    print("No cleaned text files found.")
    exit()

source_file = txt_files[0]

print(f"Processing: {source_file.name}")

with open(source_file, "r", encoding="utf-8") as f:
    text = f.read()

# Detect chapter headings
pattern = r"(Chapter\s+\d+\.[^\n]*)"

matches = list(re.finditer(pattern, text))

print(f"Found {len(matches)} chapters")

for i, match in enumerate(matches):

    chapter_title = match.group(1).strip()

    start = match.start()

    if i < len(matches) - 1:
        end = matches[i + 1].start()
    else:
        end = len(text)

    chapter_text = text[start:end]

    chapter_number = str(i + 1).zfill(2)

    filename = f"Chapter_{chapter_number}.txt"

    output_file = output_dir / filename

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(chapter_text)

    print(f"Saved: {filename}")
