from services.ingredient_service import decode_ingredients


sample_text = """
Ingredients:
Wheat Flour, Sugar, Vegetable Oil,
INS 330, INS 322, INS 500
"""


results = decode_ingredients(sample_text)


print("\n===== INGREDIENT DECODER =====\n")

for ingredient in results:

    print(f"Code: {ingredient['code']}")
    print(f"Name: {ingredient['name']}")
    print(f"Category: {ingredient['category']}")
    print(f"Explanation: {ingredient['explanation']}")
    print(f"Common uses: {ingredient['common_uses']}")
    print("-" * 50)