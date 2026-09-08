from services.ocr_service import extract_text
from services.nutrition_service import extract_nutrition


image_path = "biscuit.jpg"

ocr_text = extract_text(image_path)

nutrition = extract_nutrition(ocr_text)

print("\n===== EXTRACTED NUTRITION =====\n")

for nutrient, value in nutrition.items():
    print(f"{nutrient}: {value}")