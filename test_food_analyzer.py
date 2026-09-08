from services.food_analyzer import analyze_food_label


image_path = "biscuit.jpg"

result = analyze_food_label(image_path)


print("\n===== FOOD LABEL ANALYSIS =====\n")

print("SERVING INFORMATION")
print(result["serving_info"])

print("\nNUTRITION")
for nutrient, value in result["nutrition"].items():
    print(f"{nutrient}: {value}")

print("\nNUTRITION ANALYSIS")
print(result["nutrition_analysis"])

print("\nINGREDIENTS / ADDITIVES")
for ingredient in result["ingredients"]:
    print(
        f"{ingredient['code']} → "
        f"{ingredient['name']}"
    )

print("\nALLERGENS")

if result["allergens"]:

    for allergen, matches in result["allergens"].items():
        print(
            f"{allergen}: "
            f"{', '.join(matches)}"
        )

else:
    print("No supported allergens detected.")