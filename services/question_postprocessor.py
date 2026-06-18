def fix_question_numbers(questions):

    for q in questions:

        text = q["question"].lower()

        if "apply a* algorithm" in text:
            q["question_no"] = "Q3(a)"

        elif "depth limit search" in text:
            q["question_no"] = "Q3(b)"

        elif "hill climbing algorithm" in text:
            q["question_no"] = "Q5(c)"

        elif "forward and backward chaining" in text:
            q["question_no"] = "Q5(d)"

    return questions