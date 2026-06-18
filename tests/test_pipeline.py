from services.extraction_service import extract_questions
from services.bloom_service import predict_bloom
from services.question_filter import is_valid_question
from services.question_cleaner import clean_question

pdf_path = "test_files/be_computer-engineering_semester-6_2022_december_artificial-intelligencerev-2019-c-scheme.pdf"

questions = extract_questions(pdf_path)

print("Before filter:", len(questions))

questions = [
    q for q in questions
    if is_valid_question(q["question"])
]

print("After filter:", len(questions))

# Clean questions
for q in questions:
    q["question"] = clean_question(q["question"])

# Predict
results = []

for q in questions:

    bloom = predict_bloom(q["question"])

    results.append({
        "question_no": q["question_no"],
        "question": q["question"],
        "bloom_level": bloom
    })

print(results)