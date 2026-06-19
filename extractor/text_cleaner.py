import re

def clean_ocr_text(text):

    text = re.sub(
    r'Q\s*([1-6])\s*([a-f])',
    r'\nQ\1\n\2\n',
    text,
    flags=re.IGNORECASE
    )
    text = re.sub(
        r'Page\s+\d+\s+of\s+\d+',
        '',
        text,
        flags=re.IGNORECASE
    )

    text = re.sub(
        r'\[\d+\]',
        '',
        text
    )

    # Remove watermark garbage
    text = re.sub(
        r'\b[A-Z0-9]{8,}\b',
        '',
        text
    )

    # Remove long standalone numbers
    text = re.sub(
        r'\b\d{4,}\b',
        '',
        text
    )

    # Convert "2 a" -> "2\na"
    text = re.sub(
        r'\n([1-9])\s+([a-f])\s*\n',
        r'\n\1\n\2\n',
        text,
        flags=re.IGNORECASE
    )

    # Convert "b What is..." -> "b\nWhat is..."
    text = re.sub(
        r'\n([a-f])\s+([A-Z])',
        r'\n\1\n\2',
        text
    )

    # Clean spaces but KEEP newlines
    text = re.sub(r'[ \t]+', ' ', text)

    # Remove excessive blank lines
    text = re.sub(r'\n\s*\n+', '\n', text)

    text = re.sub(r'φ\(\d+\)', ' ', text)
    # Put question markers on separate lines

    text = re.sub(
        r'(Q\d+\s*[a-f]\))',
        r'\n\1\n',
        text,
        flags=re.IGNORECASE
    )

    text = re.sub(
        r'(Q\d+[a-f]\))',
        r'\n\1\n',
        text,
        flags=re.IGNORECASE
    )

    text = re.sub(
        r'([1-9]\s*[a-f]\))',
        r'\n\1\n',
        text,
        flags=re.IGNORECASE
    )

    text = re.sub(
        r'([1-9][a-f]\))',
        r'\n\1\n',
        text,
        flags=re.IGNORECASE
    )

    text = re.sub(r'\n+', '\n', text)

    return text.strip()