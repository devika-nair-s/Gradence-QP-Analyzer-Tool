import fitz
from paddleocr import PaddleOCR
import tempfile
import os

ocr = PaddleOCR(
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    use_textline_orientation=False
)

def extract_scanned_pdf(pdf_path):
    """
    Extract text from scanned university papers using
    PyMuPDF + PaddleOCR.
    """

    doc = fitz.open(pdf_path)

    all_text = []

    for page_num in range(len(doc)):
        page = doc[page_num]

        pix = page.get_pixmap(matrix=fitz.Matrix(3, 3))

        with tempfile.NamedTemporaryFile(
            suffix=".png",
            delete=False
        ) as temp_img:

            image_path = temp_img.name

        pix.save(image_path)

        results = ocr.predict(image_path)

        page_text = []

        for result in results:
            page_text.extend(result["rec_texts"])

        all_text.append("\n".join(page_text))

        os.remove(image_path)

    doc.close()

    return "\n".join(all_text)
