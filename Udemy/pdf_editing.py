"""
The PyPDF2 module can read and write PDFs.
Opening a PDF is done by calling open() and passing the file object to PPdfFileReader().
A Page object can be obtained from the PDF object with the getPage() method.
The text from a Page object is obtained with the extractText() method, which can be imperfect.
New PDFs can be made from PdfFileWriter().
New pages can be appended to a writer object with the addPage() method.
Call the write() method to save its changes.
"""

