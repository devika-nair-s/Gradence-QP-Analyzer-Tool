import os
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline

# --------------------------------------------------
# Load dataset
# --------------------------------------------------

df = pd.read_csv("data/blooms_taxonomy_dataset.csv")

print("Columns:", df.columns)
print("Dataset Size:", len(df))

X = df["Questions"]
y = df["Category"]

print(df["Category"].value_counts())

# --------------------------------------------------
# Train / Test Split
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# --------------------------------------------------
# Pipeline
# --------------------------------------------------

model = Pipeline([
    (
        "tfidf",
        TfidfVectorizer(
            lowercase=True,
            stop_words="english",
            ngram_range=(1, 2),
            max_features=10000
        )
    ),
    (
        "classifier",
        LogisticRegression(
            max_iter=2000,
            class_weight="balanced"
        )
    )
])

# --------------------------------------------------
# Train
# --------------------------------------------------

print("Training...")

model.fit(X_train, y_train)

print("Training Complete")

# --------------------------------------------------
# Evaluate
# --------------------------------------------------

predictions = model.predict(X_test)

print("\nClassification Report:\n")

print(
    classification_report(
        y_test,
        predictions
    )
)

# --------------------------------------------------
# Save
# --------------------------------------------------

os.makedirs(
    "models/bloom_classifier",
    exist_ok=True
)

joblib.dump(
    model,
    "models/bloom_classifier/bloom_model.pkl"
)

print(
    "\nSaved model to models/bloom_classifier/bloom_model.pkl"
)