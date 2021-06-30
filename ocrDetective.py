import subprocess
from sys import stderr
import os
from datetime import datetime

path = input('Copy and past the directory ')

now = datetime.now()
date_time = now.strftime("%Y-%m-%d at %H:%M:%S")
start_message = f'+++ As of {date_time} ocrDetective suspects these files do not contain OCR +++'

suspects = []
suspects.append(start_message)

for root, dirs, files in os.walk(path, topdown=False):
    for name in files:
        filepath = os.path.join(root, name)
        with subprocess.Popen(["pdffonts", filepath], stdout=subprocess.PIPE, stderr=subprocess.PIPE) as proc:
            out = proc.stdout.readlines()
            out_error = proc.stderr.readlines()
            font_count = len(out)

# Subtract 2 because pdffonts includes two initial lines as a heading
        if font_count - 2 == 0:
            print(filepath)
            suspects.append(filepath)
        else:
            pass

output_txt = os.path.join(path, "suspects.txt")

print(suspects)
with open(output_txt, "w") as f:
    for suspect in suspects:
        f.write("%s\n" % suspect)
