from services.ocr_service import extract_text
from services.nutrition_service import extract_nutrition
from services.serving_service import extract_serving_info
from services.ingredient_service import decode_ingredients
from services.allergen_service import detect_allergens
from services.analysis_service import analyze_nutrition


def analyze_food_label(image_path):
    """
    Complete food-label analysis pipeline.
    """

    # 1. OCR
    ocr_text = extract_text(image_path)

    # 2. Nutrition extraction
    nutrition = extract_nutrition(ocr_text)

    # 3. Serving information
    serving_info = extract_serving_info(ocr_text)

    # 4. Nutrition analysis
    nutrition_analysis = analyze_nutrition(
        nutrition,
        serving_info
    )

    # 5. Ingredient/additive decoder
    ingredients = decode_ingredients(ocr_text)

    # 6. Allergen detection
    allergens = detect_allergens(ocr_text)

    return {
        "ocr_text": ocr_text,
        "nutrition": nutrition,
        "serving_info": serving_info,
        "nutrition_analysis": nutrition_analysis,
        "ingredients": ingredients,
        "allergens": allergens
    }