import fitz  # PyMuPDF


def detect_pdf_type(pdf_path, sample_pages=3):
    """
    Detect whether a PDF contains embedded text or is scanned.

    Returns:
        'text'     -> searchable PDF
        'scanned'  -> image-based PDF
    """

    try:
        doc = fitz.open(pdf_path)

        extracted_text = ""

        # Check only first few pages for speed
        pages_to_check = min(sample_pages, len(doc))

        for page_num in range(pages_to_check):
            page = doc[page_num]
            extracted_text += page.get_text()

        doc.close()

        # Clean whitespace
        extracted_text = extracted_text.strip()

        # If enough text exists, treat as text PDF
        if len(extracted_text) > 100:
            return "text"

        return "scanned"

    except Exception as e:
        print(f"PDF detection error: {e}")
        return "unknown"