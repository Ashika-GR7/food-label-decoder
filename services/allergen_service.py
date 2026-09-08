import re


ALLERGENS = {
    "Milk": [
        "milk powder",
        "milk solids",
        "milk",
        "whey",
        "casein",
        "caseinate",
        "lactose"
    ],

    "Wheat": [
        "wheat flour",
        "wheat starch",
        "wheat",
        "gluten"
    ],

    "Soy": [
        "soy lecithin",
        "soybean",
        "soya",
        "soy"
    ],

    "Egg": [
        "egg white",
        "egg yolk",
        "egg",
        "albumin"
    ],

    "Peanut": [
        "peanut",
        "groundnut"
    ],

    "Tree Nuts": [
        "almond",
        "cashew",
        "walnut",
        "pistachio",
        "hazelnut",
        "pecan"
    ],

    "Sesame": [
        "sesame seed",
        "sesame"
    ]
}


def detect_allergens(text):
    """
    Detect common allergens and return the
    most specific matching terms.
    """

    detected = {}

    text_lower = text.lower()

    for allergen, keywords in ALLERGENS.items():

        # Check longer phrases first
        sorted_keywords = sorted(
            keywords,
            key=len,
            reverse=True
        )

        matches = []

        for keyword in sorted_keywords:

            pattern = r"\b" + re.escape(keyword) + r"\b"

            if re.search(pattern, text_lower):

                # Avoid adding a shorter match when
                # a longer phrase already matched.
                if not any(
                    keyword in existing
                    for existing in matches
                ):
                    matches.append(keyword)

        if matches:
            detected[allergen] = matches

    return detected