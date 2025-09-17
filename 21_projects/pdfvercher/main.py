from PyPDF2 import PdfWriter

merger = PdfWriter()

pdf = []
n = int(input("How many pdf do you wamt marge?:\n "))

for i in range(0, n):
    name = str(input(f"Enter the pdf {i + 1}: "))
    pdf.append(name)


merger.write("merged-pdf.pdf")
merger.close()