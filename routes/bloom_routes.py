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

        result = extract_questions(
            temp_pdf.name
        )

        subject = result["subject"]
        questions = result["questions"]

        print("\nSUBJECT:", subject)
        print("TOTAL QUESTIONS:", len(questions))

        print("\n===== RAW QUESTIONS =====")

        for i, q in enumerate(questions):
            print(i, type(q), q)

        filtered = []

        for q in questions:

            print("ITEM:", q)
            print("TYPE:", type(q))

            if isinstance(q, dict):

                if is_valid_question(q["question"]):
                    filtered.append(q)

        questions = filtered

        predictions = []
        co_mapping = []
        cleaned_questions = []

        for q in questions:
            print("\nCURRENT Q:")
            print(q)
            print(type(q))

            cleaned = clean_question(
                q["question"]
            )
            print("CLEANED:")
            print(cleaned)
            print(type(cleaned))

            bloom = predict_bloom(
                cleaned
            )

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

        return jsonify({
            "total_questions": len(cleaned_questions),
            "overall_difficulty": overall,
            "questions": cleaned_questions,
            "predictions": predictions,
            "co_mapping": co_mapping
        })

    except Exception as e:

        print("\n===== ERROR =====")
        traceback.print_exc()

        return jsonify({
            "error": str(e)
        }), 500

    finally:

        if os.path.exists(temp_pdf.name):
            os.remove(temp_pdf.name)

