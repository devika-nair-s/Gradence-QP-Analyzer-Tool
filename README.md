# Gradence – AI-Powered Question Paper Analyzer

Gradence is an AI-powered academic analytics tool that automatically extracts questions from university examination papers and analyzes them using Bloom's Taxonomy and Course Outcome (CO) mapping.

The system supports both searchable PDFs and scanned question papers through OCR-based text extraction.

---

## Features

### Question Extraction

* Extracts questions from PDF question papers
* Supports:

  * Text-based PDFs
  * Scanned PDFs using OCR
* Automatically detects PDF type

### Bloom's Taxonomy Classification

* Classifies each question into:

  * BT1 – Remember
  * BT2 – Understand
  * BT3 – Apply
  * BT4 – Analyze
  * BT5 – Evaluate
  * BT6 – Create

### Subject Detection

* Identifies the subject from the uploaded question paper
* Supports multiple engineering subjects

### Course Outcome (CO) Mapping

* Maps questions to predefined Course Outcomes
* Subject-specific keyword matching

### Assessment Analytics

* Total questions count
* Bloom's level distribution
* Overall paper difficulty analysis
* Question-wise CO mapping

---

## Tech Stack

### Backend

* Python
* Flask

### AI / NLP

* DistilBERT
* Custom Bloom Classification Model

### OCR

* PaddleOCR
* PyMuPDF

### Frontend

* HTML
* CSS
* JavaScript

### Data Storage

* JSON-based CO mappings

---

## Project Structure

```text
Gradence Final/
│
├── app.py
├── routes/
├── services/
├── extractor/
├── models/
├── static/
├── templates/
├── data/
├── test_files/
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/devika-nair-s/Gradence-QP-Analyzer-Tool.git

cd Gradence-QP-Analyzer-Tool
```

### Create Virtual Environment

```bash
python3 -m venv venv

source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
python3 app.py
```

Application runs on:

```text
http://127.0.0.1:5000
```

---

## Workflow

1. Upload question paper
2. Detect PDF type
3. Extract text
4. Clean OCR noise
5. Parse questions
6. Detect subject
7. Classify Bloom's level
8. Map Course Outcomes
9. Generate analytics report

---

## Sample Output

For each extracted question:

* Question Text
* Bloom's Taxonomy Level
* Subject
* Course Outcome Mapping

Example:

```text
Question:
Explain Diffie Hellman key exchange.

Bloom Level:
BT2

CO:
CO3 – Cryptographic Key Management
```

---

## Future Enhancements

* LLM-powered question understanding
* Automatic syllabus extraction
* CO mapping using semantic similarity
* Question difficulty prediction
* Department-wise analytics dashboard
* Export reports as PDF

---

## Author

Devika Nair

AI-powered academic assessment and question paper analysis project developed as part of engineering coursework and research.
