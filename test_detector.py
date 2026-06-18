from extractor.pdf_detector import detect_pdf_type

pdf_path = "test_files/be_computer-engineering_semester-6_2022_december_artificial-intelligencerev-2019-c-scheme.pdf"

result = detect_pdf_type(pdf_path)

print("PDF Type:", result)