import re


def extract_serving_info(text):
    """
    Extract serving size information from OCR text.
    """

    result = {
        "serving_size": None,
        "serving_unit": None,
        "basis": "unknown"
    }

    lines = text.splitlines()

    for line in lines:

        normalized = line.lower().strip()

        # Detect serving size
        if "serving size" in normalized:

            match = re.search(
                r"(\d+(?:\.\d+)?)\s*(g|mg|kg|ml|l|oz)",
                normalized,
                re.IGNORECASE
            )

            if match:
                result["serving_size"] = float(match.group(1))
                result["serving_unit"] = match.group(2)

        # Detect nutrition basis
        if "per 100 g" in normalized or "per 100g" in normalized:
            result["basis"] = "per 100 g"

        elif "per 100 ml" in normalized or "per 100ml" in normalized:
            result["basis"] = "per 100 ml"

        elif "per serving" in normalized:
            result["basis"] = "per serving"

    # If serving size was found but no explicit basis,
    # nutrition facts are usually presented per serving.
    if result["serving_size"] is not None and result["basis"] == "unknown":
        result["basis"] = "per serving"

    return result