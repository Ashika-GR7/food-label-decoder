def classify_sugar(value):
    if value is None:
        return "Unknown"

    if value <= 5:
        return "Low"

    elif value <= 22.5:
        return "Moderate"

    return "High"


def classify_fat(value):
    if value is None:
        return "Unknown"

    if value <= 3:
        return "Low"

    elif value <= 17.5:
        return "Moderate"

    return "High"


def classify_sodium(value):
    if value is None:
        return "Unknown"

    if value <= 120:
        return "Low"

    elif value <= 600:
        return "Moderate"

    return "High"


def classify_protein(value):
    if value is None:
        return "Unknown"

    if value >= 10:
        return "Good"

    elif value >= 5:
        return "Moderate"

    return "Low"


def classify_nutrition(nutrition):
    """
    Apply predefined classification rules.

    Values are expected to be on a per-100-g basis.
    """

    return {
        "sugar": classify_sugar(
            nutrition.get("sugar")
        ),

        "fat": classify_fat(
            nutrition.get("total_fat")
        ),

        "sodium": classify_sodium(
            nutrition.get("sodium")
        ),

        "protein": classify_protein(
            nutrition.get("protein")
        )
    }