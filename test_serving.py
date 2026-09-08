from services.ocr_service import extract_text
from services.serving_service import extract_serving_info


image_path = "biscuit.jpg"

ocr_text = extract_text(image_path)

serving_info = extract_serving_info(ocr_text)

print("\n===== SERVING INFORMATION =====\n")

for key, value in serving_info.items():
    print(f"{key}: {value}")