import re


def is_valid_question(text):

    text = text.strip()

    if len(text) < 20:
        return False

    # Reject page headers
    if "paper / subject code" in text.lower():
        return False

    if "page " in text.lower():
        return False

    # Reject graph labels
    if re.fullmatch(r'[A-Z0-9+\s]+', text):
        return False

    # Reject instruction text
    bad_phrases = [
        "solve any",
        "note:",
        "max marks",
        "time:",
        "write detailed note on following",
        "any two",
        "any four"
    ]

    for phrase in bad_phrases:
        if phrase in text.lower():
            return False

    return True