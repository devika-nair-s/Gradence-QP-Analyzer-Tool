import fitz

pdf_path = "test_files/be_computer-engineering_semester-6_2022_december_artificial-intelligencerev-2019-c-scheme.pdf"

doc = fitz.open(pdf_path)

page = doc[0]

pix = page.get_pixmap(matrix=fitz.Matrix(3, 3))

pix.save("page1.png")

doc.close()

print("Saved page1.png")