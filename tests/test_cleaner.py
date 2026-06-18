from extractor.scanned_pdf import extract_scanned_pdf
from extractor.text_cleaner import clean_ocr_text

pdf_path = "test_files/be_computer-engineering_semester-6_2022_december_artificial-intelligencerev-2019-c-scheme.pdf"

text = extract_scanned_pdf(pdf_path)

cleaned = clean_ocr_text(text)

print(cleaned)