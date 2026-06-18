from paddleocr import PaddleOCR

ocr = PaddleOCR(
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    use_textline_orientation=False
)

results = ocr.predict("page1.png")

page = results[0]

texts = page["rec_texts"]
boxes = page["rec_boxes"]

for text, box in zip(texts, boxes):

    x = box[0]

    # Ignore watermark region
    if x > 900:
        continue

    print(text)