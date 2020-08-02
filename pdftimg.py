import fitz


#pdffile = "imgupld/testp.pdf"
def convert(pdffile):
	doc = fitz.open(pdffile)
	x=0
	x=len(doc)
	print(x)
	for i in range(x):
	    page = doc.loadPage(i) #number of page
	    pix = page.getPixmap()
	    output = "pdf/outfile"+str(i)+".jpg"
	    pix.writePNG(output)