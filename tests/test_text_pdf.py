from extractor.text_pdf import extract_text_pdf

pdf_path = "test_files/be_computer-engineering_semester-6_2023_may_cryptography-system-securityrev-2019-c-scheme.pdf"

text = extract_text_pdf(pdf_path)

print(text[:5000])