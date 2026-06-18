import fitz

pdf_path = "test_files/be_computer-engineering_semester-6_2022_december_artificial-intelligencerev-2019-c-scheme.pdf"

doc = fitz.open(pdf_path)

for page_num in range(len(doc)):
    page = doc[page_num]

    text = page.get_text()

    print("\n" + "=" * 50)
    print(f"PAGE {page_num + 1}")
    print("=" * 50)

    print(text[:3000])  # first 3000 chars only

doc.close()