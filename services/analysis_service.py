from services.classification_service import classify_nutrition


def analyze_nutrition(nutrition, serving_info):
    """
    Analyze nutrition only when values are suitable
    for the classification rules.
    """

    basis = serving_info.get("basis")

    if basis != "per 100 g":
        return {
            "classification_available": False,
            "message": (
                "Nutrition values are not reported per 100 g. "
                "Values are shown without applying the "
                "project's per-100-g classification rules."
            ),
            "levels": {}
        }

    levels = classify_nutrition(nutrition)

    return {
        "classification_available": True,
        "message": "Classification based on per-100-g values.",
        "levels": levels
    }