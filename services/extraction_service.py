from extractor.pdf_detector import detect_pdf_type
from extractor.text_pdf import extract_text_pdf
from extractor.scanned_pdf import extract_scanned_pdf

from services.subject_detector import detect_subject
from extractor.text_cleaner import clean_ocr_text
from extractor.question_parser import parse_questions


def extract_questions(pdf_path):

    pdf_type = detect_pdf_type(pdf_path)

    print(f"\nPDF TYPE: {pdf_type}")

    if pdf_type == "text":

        print("Using TEXT extraction")

        raw_text = extract_text_pdf(pdf_path)

    else:

        print("Using OCR extraction")

        raw_text = extract_scanned_pdf(pdf_path)

    # SUBJECT DETECTION HERE
    subject = detect_subject(raw_text)

    print("SUBJECT:", subject)
    print("\n===== DETECTED SUBJECT =====")
    print(subject)

    cleaned_text = clean_ocr_text(raw_text)

    questions = parse_questions(cleaned_text)

    return {
    "subject": subject,
    "questions": questions
}