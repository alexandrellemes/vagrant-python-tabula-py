#!/usr/bin/python

import tabula

# Read pdf into list of DataFrame
dfs = tabula.read_pdf("test.pdf", pages='all')

# Read remote pdf into list of DataFrame
dfs2 = tabula.read_pdf("https://github.com/tabulapdf/tabula-java/raw/master/src/test/resources/technology/tabula/arabic.pdf")

# convert PDF into CSV file
tabula.convert_into("test.pdf", "output.csv", output_format="csv", pages='all')

# convert all PDFs in a directory
tabula.convert_into_by_batch("pdf_directory", output_format='csv', pages='all')