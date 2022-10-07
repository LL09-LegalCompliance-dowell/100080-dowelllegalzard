from xhtml2pdf import pisa
import os


def generate_pdf(sourceHtml, outputFilename):
	# open output file for writing (truncated binary)
	resultFile = open(outputFilename, "w+b")
	# convert HTML to PDF
	# the HTML to convert [sourceHtml]
	pisaStatus = pisa.CreatePDF(sourceHtml,dest=resultFile)
	# close output file
	resultFile.close()
	# return True on success and False on errors
	return pisaStatus.err