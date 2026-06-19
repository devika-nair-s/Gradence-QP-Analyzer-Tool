from flask import Blueprint, request, jsonify
import tempfile
import os
import traceback
from collections import Counter

from services.extraction_service import extract_questions
from services.bloom_service import predict_bloom
from services.question_filter import is_valid_question
from services.question_cleaner import clean_question
from services.co_mapper import map_question_to_co

bloom_bp = Blueprint("bloom", __name__)


@bloom_bp.route("/analyze", methods=["POST"])
def analyze_paper():

    if "file" not in request.files:
        return jsonify({
            "error": "No file uploaded"
        }), 400

    uploaded_file = request.files["file"]

    temp_pdf = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    )

    uploaded_file.save(temp_pdf.name)

    try:

        result = extract_questions(temp_pdf.name)

        subject = result.get("subject", "Unknown Subject")
        questions = result.get("questions", [])

        print("\n==============================")
        print("SUBJECT:", subject)
        print("TOTAL EXTRACTED:", len(questions))
        print("==============================")

        print("\n===== RAW QUESTIONS =====")

        for i, q in enumerate(questions):
            print(i, type(q), q)

        # ---------------- FILTER ----------------

        filtered = []

        for q in questions:

            if not isinstance(q, dict):
                print("SKIPPED (not dict):", q)
                continue

            question_text = q.get("question", "").strip()

            print("\nCHECKING QUESTION:")
            print(question_text[:150])

            valid = is_valid_question(question_text)

            print("VALID =", valid)

            if valid:
                filtered.append(q)

        questions = filtered

        print("\n===== AFTER FILTER =====")
        print("TOTAL AFTER FILTER:", len(questions))

        for q in questions:
            print(q)

        # ---------------- ANALYSIS ----------------

        predictions = []
        co_mapping = []
        cleaned_questions = []

        for q in questions:

            cleaned = clean_question(
                q.get("question", "")
            )

            print("\nCLEANED QUESTION:")
            print(cleaned)

            bloom = predict_bloom(cleaned)

            co = map_question_to_co(
                cleaned,
                subject
            )

            cleaned_questions.append(cleaned)
            predictions.append(bloom)
            co_mapping.append(co)

        counter = Counter(predictions)

        overall = (
            counter.most_common(1)[0][0]
            if counter
            else "Unknown"
        )

        print("\n===== RESPONSE =====")
        print("TOTAL QUESTIONS =", len(cleaned_questions))
        print("OVERALL =", overall)

        response = {
            "total_questions": len(cleaned_questions),
            "overall_difficulty": overall,
            "questions": cleaned_questions,
            "predictions": predictions,
            "co_mapping": co_mapping,
            "subject": subject
        }

        print(response)

        return jsonify(response)

    except Exception as e:

        print("\n===== ERROR =====")
        traceback.print_exc()

        return jsonify({
            "error": str(e)
        }), 500

    finally:

        if os.path.exists(temp_pdf.name):
            os.remove(temp_pdf.name)