from services.allergen_service import detect_allergens


sample_text = """
Ingredients:
Wheat Flour, Sugar, Milk Solids,
Soy Lecithin, Cocoa Powder,
Sesame Seeds
"""


allergens = detect_allergens(sample_text)


print("\n===== ALLERGEN DETECTION =====\n")

if allergens:

    for allergen, matches in allergens.items():

        print(f"{allergen}: {', '.join(matches)}")

else:

    print("No supported allergens detected.")