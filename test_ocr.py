from services.ocr_service import extract_text


image_path = "biscuit.jpg"

text = extract_text(image_path)

print("\n===== PREPROCESSED OCR RESULT =====\n")
print(text)