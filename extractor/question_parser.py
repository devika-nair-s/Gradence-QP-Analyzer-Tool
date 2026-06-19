import re

def parse_questions(text):

    questions = []

    current_main = None
    current_sub = None
    current_text = []

    lines = text.splitlines()

    for line in lines:

        line = line.strip()

        if not line:
            continue

        # Q1 / Q2 / Q3
        q_match = re.match(
            r'^Q\s*(\d+)\.?',
            line,
            re.IGNORECASE
        )

        if q_match:

            if current_main and current_sub and current_text:

                questions.append({
                    "question_no": f"Q{current_main}({current_sub})",
                    "question": " ".join(current_text).strip()
                })

            current_main = q_match.group(1)
            current_sub = None
            current_text = []
            continue

        # a. b. c. d.
        sub_match = re.match(
            r'^([a-f])[\.\)]?\s*(.*)',
            line,
            re.IGNORECASE
        )

        if sub_match:

            if current_main and current_sub and current_text:

                questions.append({
                    "question_no": f"Q{current_main}({current_sub})",
                    "question": " ".join(current_text).strip()
                })

            current_sub = sub_match.group(1).lower()

            first_text = sub_match.group(2).strip()

            current_text = []

            if first_text:
                current_text.append(first_text)

            continue

        if current_sub:
            current_text.append(line)

    if current_main and current_sub and current_text:

        questions.append({
            "question_no": f"Q{current_main}({current_sub})",
            "question": " ".join(current_text).strip()
        })

    return questions