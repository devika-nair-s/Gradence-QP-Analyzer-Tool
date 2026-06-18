import re


def clean_question(question):

    # Remove trailing standalone numbers
    question = re.sub(
        r'\s+\d+\s*$',
        '',
        question
    )

    # Remove graph remnants
    question = re.sub(
        r'\s+[+\-]?\s*\d+(?:\s+\d+)*$',
        '',
        question
    )
    
    # Remove paper header
    question = re.sub(
        r'Paper\s*/\s*Subject\s*Code.*',
        '',
        question,
        flags=re.IGNORECASE
    )

    # Remove page numbers
    question = re.sub(
        r'Page\s+\d+\s+of\s+\d+',
        '',
        question,
        flags=re.IGNORECASE
    )

    # Remove marks
    question = re.sub(
        r'\[\d+\]',
        '',
        question
    )

    # Remove watermark codes
    question = re.sub(
        r'\b[A-Z]{1,4}\d+[A-Z0-9]*\b',
        '',
        question
    )

    # Remove standalone numbers
    question = re.sub(
        r'\b\d{4,}\b',
        '',
        question
    )

    # Remove graph fragments at end of question
    question = re.sub(
        r'\b[A-GS]\b(?:\s+\b[A-GS]\b)+',
        '',
        question
    )

    # Remove repeated punctuation
    question = re.sub(
        r'\.{2,}',
        '.',
        question
    )

    # Remove repeated spaces
    question = re.sub(
        r'\s+',
        ' ',
        question
    )

    return question.strip()