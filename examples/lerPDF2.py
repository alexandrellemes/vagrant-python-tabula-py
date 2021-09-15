#!/usr/bin/python

import PyPDF2

pdf_file = open('data.pdf', 'rb')

read_pdf = PyPDF2.PdfFileReader(pdf_file)

page = read_pdf.getPage(0)

page_content = page.extractText()

pdf = page_content.encode('utf-8')

print(pdf)