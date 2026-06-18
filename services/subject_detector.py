# services/subject_detector.py

import re


KNOWN_SUBJECTS = [
    "Artificial Intelligence",
    "Cryptography & System Security",
    "Mobile Computing",
    "Data Warehousing and Mining",
    "Software Engineering",
    "Computer Networks",
    "Machine Learning",
    "Big Data Analytics",
    "Cloud Computing"
]


def detect_subject(text):

    # Method 1:
    # Extract from "Paper / Subject Code"

    match = re.search(
        r'Paper\s*/\s*Subject\s*Code\s*:.*?/\s*([A-Za-z& ]+)',
        text,
        re.IGNORECASE
    )

    if match:
        subject = match.group(1).strip()

        for known in KNOWN_SUBJECTS:
            if known.lower() in subject.lower():
                return known

    # Method 2:
    # Search full text for known subjects

    text_lower = text.lower()

    for subject in KNOWN_SUBJECTS:
        if subject.lower() in text_lower:
            return subject
    # Handle common aliases

    if "mobile computing" in text_lower:
        return "Mobile Computing & Communication"

    if "cryptography" in text_lower:
        return "Cryptography & System Security"

    if "artificial intelligence" in text_lower:
        return "Artificial Intelligence"

    if "database management" in text_lower:
        return "Database Management Systems"

    if "compiler construction" in text_lower:
        return "System Programming & Compiler Construction"

    return "Unknown Subject"