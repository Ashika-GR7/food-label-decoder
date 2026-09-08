import json
import re


DATABASE_PATH = "data/ingredients.json"


def load_ingredient_database():
    """
    Load the ingredient/additive database.
    """

    with open(DATABASE_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def find_additive_codes(text):
    """
    Find INS additive codes in OCR text.
    """

    pattern = r"\bINS\s*\d{3,4}\b"

    matches = re.findall(
        pattern,
        text,
        re.IGNORECASE
    )

    return matches


def normalize_code(code):
    """
    Normalize INS codes into a consistent format.
    """

    number = re.search(r"\d{3,4}", code)

    if number:
        return f"INS {number.group()}"

    return code


def decode_ingredients(text):
    """
    Find and decode known INS additive codes.
    """

    database = load_ingredient_database()

    detected_codes = find_additive_codes(text)

    results = []

    for code in detected_codes:

        normalized_code = normalize_code(code)

        if normalized_code in database:

            ingredient = database[normalized_code]

            results.append({
                "code": normalized_code,
                "name": ingredient["name"],
                "category": ingredient["category"],
                "explanation": ingredient["explanation"],
                "common_uses": ingredient["common_uses"]
            })

    return results