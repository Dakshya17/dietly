import random
import json

# Load meal data
with open("meal_data.json", "r") as f:
    MEALS = json.load(f)

def ai_suggest_meals(user_tags=None, meal_type=None, max_calories=None, n=5):
    """
    Suggest meals based on AI-like logic:
    - user_tags: list of diet preferences (e.g., ["Protein-Rich", "Vegan"])
    - meal_type: "breakfast", "lunch", "dinner", "snack", "drink"
    - max_calories: optional calorie filter
    - n: number of suggestions
    """
    suggestions = []
    
    # Flatten all meals
    all_meals = []
    for category, items in MEALS.items():
        for meal in items:
            all_meals.append(meal)
    
    # Filter by user tags
    if user_tags:
        all_meals = [m for m in all_meals if any(tag in m["tags"] for tag in user_tags)]
    
    # Filter by meal type
    if meal_type:
        all_meals = [m for m in all_meals if meal_type in m["tags"]]
    
    # Filter by calories
    if max_calories:
        all_meals = [m for m in all_meals if m["calories"] <= max_calories]
    
    # Randomly select n meals
    suggestions = random.sample(all_meals, min(n, len(all_meals)))
    
    return suggestions
