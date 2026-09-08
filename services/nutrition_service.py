import re


def clean_ocr_line(line):
    """
    Clean common OCR mistakes while preserving the text structure.
    """

    line = line.strip()

    # Common OCR confusion:
    # Omg → 0mg
    # Og  → 0g
    # Omcg → 0mcg
    line = re.sub(r"(?i)(?<=\s)O(?=\d|m|g)", "0", line)

    return line


def extract_value(line):
    """
    Extract a numeric value followed by an optional nutrition unit.
    """

    cleaned = line.replace("Omg", "0mg")
    cleaned = cleaned.replace("Og", "0g")
    cleaned = cleaned.replace("Omcg", "0mcg")

    match = re.search(
        r"(\d+(?:\.\d+)?)\s*(?:g|mg|mcg|kcal)?",
        cleaned,
        re.IGNORECASE
    )

    if match:
        return float(match.group(1))

    return None


def extract_nutrition(text):
    """
    Extract nutrition values from OCR text.
    """

    nutrition = {
        "calories": None,
        "total_fat": None,
        "saturated_fat": None,
        "trans_fat": None,
        "cholesterol": None,
        "sodium": None,
        "carbohydrates": None,
        "dietary_fiber": None,
        "sugar": None,
        "added_sugar": None,
        "protein": None
    }

    lines = text.splitlines()

    for line in lines:

        original_line = line
        line = clean_ocr_line(line)

        normalized = line.lower().strip()

        # Ignore the calorie conversion section at the bottom
        if "calories per gram" in normalized:
            continue

        if normalized.startswith("calories"):
            nutrition["calories"] = extract_value(line)

        elif normalized.startswith("total fat"):
            nutrition["total_fat"] = extract_value(line)

        elif normalized.startswith("saturated fat"):
            nutrition["saturated_fat"] = extract_value(line)

        elif normalized.startswith("trans fat"):
            nutrition["trans_fat"] = extract_value(line)

        elif normalized.startswith("cholesterol"):
            nutrition["cholesterol"] = extract_value(line)

        elif normalized.startswith("sodium"):
            nutrition["sodium"] = extract_value(line)

        elif normalized.startswith("total carbohydrate"):
            nutrition["carbohydrates"] = extract_value(line)

        elif normalized.startswith("dietary fiber"):
            nutrition["dietary_fiber"] = extract_value(line)

        elif normalized.startswith("total sugars"):
            nutrition["sugar"] = extract_value(line)

        elif normalized.startswith("includes") and "added sugar" in normalized:
            nutrition["added_sugar"] = extract_value(line)

        elif normalized.startswith("protein"):
            nutrition["protein"] = extract_value(line)

    return nutrition