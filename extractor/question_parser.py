import re


def clean_text(text):
    """
    Remove watermark garbage and unnecessary text.
    """

    # Remove long watermark codes
    text = re.sub(r'\b[A-Z0-9]{10,}\b', ' ', text)

    # Remove page numbers
    text = re.sub(r'Page\s+\d+\s+of\s+\d+', ' ', text, flags=re.IGNORECASE)

    # Remove repeated spaces
    text = re.sub(r'[ \t]+', ' ', text)
    
    return text.strip()


import re

import re


def parse_questions(text):

    text = clean_text(text)

    questions = []

    current_q = None

    lines = text.splitlines()

    i = 0

    while i < len(lines):

        line = lines[i].strip()

        # Detect Q1. or Q2.
        if re.match(r'^Q\d+\.?$', line, re.IGNORECASE):
            current_q = line.replace(".", "")
            i += 1
            continue

        # Detect plain 1,2,3,4,5,6
        if re.match(r'^[1-6]$', line):
            current_q = f"Q{line}"
            i += 1
            continue

        # Detect a,b,c,d,e,f
        if re.match(r'^[a-f]\.?$', line, re.IGNORECASE):

            sub = line[0].lower()

            question_text = []

            i += 1

            while i < len(lines):

                next_line = lines[i].strip()

                # Stop when next question starts
                if re.match(r'^[a-f]\.?$', next_line, re.IGNORECASE):
                    break

                if re.match(r'^Q\d+\.?$', next_line, re.IGNORECASE):
                    break

                if re.match(r'^[1-6]$', next_line):
                    break

                question_text.append(next_line)

                i += 1

            questions.append({
                "question_no": f"{current_q}({sub})",
                "question": " ".join(question_text).strip()
            })

            continue

        i += 1

    return questions

from extractor.scanned_pdf import extract_scanned_pdf
from extractor.text_cleaner import clean_ocr_text
from extractor.question_parser import parse_questions
from services.question_postprocessor import fix_question_numbers

pdf_path = "test_files/be_computer-engineering_semester-6_2022_december_artificial-intelligencerev-2019-c-scheme.pdf"

raw_text = extract_scanned_pdf(pdf_path)

cleaned_text = clean_ocr_text(raw_text)

questions = parse_questions(cleaned_text)

# NEW LINE
questions = fix_question_numbers(questions)
