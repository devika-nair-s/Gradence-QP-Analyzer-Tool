import joblib

model = joblib.load(
    "models/bloom_classifier/bloom_model.pkl"
)

def predict_bloom(question):
    return model.predict([question])[0]