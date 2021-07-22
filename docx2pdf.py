import glob
import os
from docx2pdf import convert

files = glob.glob('*.docx')

for f in files:
    fbasename = os.path.splitext(os.path.basename(f))[0]
    convert(f, f"new_pdfs\{fbasename}.pdf")
