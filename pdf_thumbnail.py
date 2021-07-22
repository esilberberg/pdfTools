from pdf2image import convert_from_path
import os
import glob

# Poppler must be in the same directory as pdf_thumbnail.py

path = input("Copy and paste the directory: ")

pdf_path = os.path.join(path, "*.pdf")

pdfs = glob.glob(pdf_path)

for pdf in pdfs:

    # Extract pdf title
    pdf_basename = os.path.basename(pdf)
    pdf_title = os.path.splitext(pdf_basename)[0]
    print(pdf_title)

    # Print first page to jpg
    pages = convert_from_path(
        pdf, poppler_path=r"poppler-21.03.0\Library\bin", last_page=1)

    for p in pages:
        p.save(f'{pdf_title}_TI.jpg', 'JPEG')
