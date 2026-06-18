import joblib

model = joblib.load(
    "models/bloom_classifier/bloom_model.pkl"
)

questions = [
    "Explain PAC Learning",
    "Apply A* Algorithm",
    "Design a predictive parser",
    "Compare DFS and BFS",
    "Construct a DFA for the following language"
]

for q in questions:

    pred = model.predict([q])[0]

    print()
    print("Question:", q)
    print("Prediction:", pred)