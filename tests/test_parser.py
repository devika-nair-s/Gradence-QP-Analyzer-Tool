from extractor.pdf_detector import detect_pdf_type
from extractor.text_pdf import extract_text_pdf
from extractor.scanned_pdf import extract_scanned_pdf

from extractor.text_cleaner import clean_ocr_text
from extractor.question_parser import parse_questions
from services.question_postprocessor import fix_question_numbers

pdf_path = "test_files/be_computer-engineering_semester-6_2023_may_cryptography-system-securityrev-2019-c-scheme.pdf"

pdf_type = detect_pdf_type(pdf_path)

print(f"\nPDF TYPE: {pdf_type}")

if pdf_type == "text":
    raw_text = extract_text_pdf(pdf_path)
else:
    raw_text = extract_scanned_pdf(pdf_path)

with open("raw_text.txt", "w", encoding="utf-8") as f:
    f.write(raw_text)

cleaned_text = clean_ocr_text(raw_text)

with open("cleaned_text.txt", "w", encoding="utf-8") as f:
    f.write(cleaned_text)

with open("cleaned_debug.txt", "w", encoding="utf-8") as f:
    f.write(cleaned_text)
    
print("\n===== CLEANED TEXT =====\n")
print(cleaned_text[:3000])

questions = parse_questions(cleaned_text)

questions = fix_question_numbers(questions)

print("\nEXTRACTED QUESTIONS:\n")

for q in questions:
    print(q)