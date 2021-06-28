from PyPDF2 import PdfFileWriter, PdfFileReader


def Get_Pages(s):
    if '-' in s:
        a, b = map(int, s.split('-'))
        return range(a, b+1)
    else:
        return int(s),


infile = input("Drag and drop target PDF: ")
page_range = input("Enter page range: ")
outfile_input = input("Enter desired output file name: ")

outfile = f"{outfile_input}.pdf"
pages = Get_Pages(page_range)

output = PdfFileWriter()
input_pdf = PdfFileReader(open(infile, "rb"))
output_file = open(outfile, "wb")

for p in pages:
    output.addPage(input_pdf.getPage(p - 1))  # pages as index start at 0

output.write(output_file)
