"""
Created on 2020/03/31

@author: David O. Sigthorsson (sigthorsson@gmail.com)

Make a website out of some of the COVID data and processing work in an adjacent project

"""

import os
import markdown
import codecs

# Copy plots from original project
os.system('cp ../../DOS-Covid-Code/Plots/* ./Plots/')

# Assign input/output files
md_file = "./main.md"
html_file = "./index.html"

# Read the markdown document and encoded it
input_file = codecs.open(md_file, mode="r", encoding="utf-8")
text = input_file.read()
html = markdown.markdown(text)

# Write the encoded markdown to a file
output_file = codecs.open(html_file, "w",
                          encoding="utf-8",
                          errors="xmlcharrefreplace"
)
output_file.write(html)

os.system("open "+html_file)
