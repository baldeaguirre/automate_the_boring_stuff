import PyPDF2

pdfFile =  open('meetingminutes1.pdf', 'rb')
reader = PyPDF2.PdfFileReader(pdfFile)
reader.numPages

page = reader.getPage(0)
page.extractText()

for pageNum in range(reader.numPages):
    print(reader.getPage(pageNum).extractText())