import json

with open("data/co_mapping.json", "r") as f:
    DATA = json.load(f)


def map_question_to_co(question, subject):

    print("\n===== CO MAPPER =====")
    print("SUBJECT RECEIVED:", repr(subject))

    print("\nAVAILABLE SUBJECTS:")
    print(list(DATA["co_mappings"].keys()))

    # -----------------------------
    # Find matching subject
    # -----------------------------
    subject_cos = DATA["co_mappings"].get(subject)

    # Exact match failed → try partial match
    if not subject_cos:

        for key in DATA["co_mappings"].keys():

            if subject.lower() in key.lower():
                subject_cos = DATA["co_mappings"][key]

                print("\nPARTIAL SUBJECT MATCH:")
                print(f"'{subject}' -> '{key}'")

                break

    print("MATCH FOUND:", subject_cos is not None)

    # No subject found
    if not subject_cos:
        return {
            "co_code": "N/A",
            "co_name": "Unknown Subject"
        }

    # -----------------------------
    # CO Mapping
    # -----------------------------
    q = question.lower()

    best_match = None
    best_score = 0

    for co_code, co_data in subject_cos.items():

        score = 0

        for keyword in co_data["keywords"]:

            keyword = keyword.lower()

            if keyword in q:
                score += 3

                print(
                    f"Matched keyword '{keyword}' "
                    f"for {co_code}"
                )

        if score > best_score:

            best_score = score

            best_match = {
                "co_code": co_code,
                "co_name": co_data["name"]
            }

    print("BEST SCORE:", best_score)
    print("BEST MATCH:", best_match)

    if best_match:
        return best_match

    return {
        "co_code": "N/A",
        "co_name": "Not Matched"
    }