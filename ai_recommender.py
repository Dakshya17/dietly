import json
from typing import List, Dict
import random

# Load meal data
with open("meal_data.json") as f:
    meal_data = json.load(f)

def recommend_meals(diet_type: str, meal_type: str, max_calories: int = None, top_n: int = 5) -> List[Dict]:
    """
    Recommend meals for a given diet type and meal type.
    Optionally filter by max_calories and return top_n meals randomly.
    """
    if diet_type not in meal_data:
        return []

    # Filter by meal_type
    filtered = [meal for meal in meal_data[diet_type] if meal_type in meal['tags']]

    # Filter by max_calories if provided
    if max_calories is not None:
        filtered = [meal for meal in filtered if meal['calories'] <= max_calories]

    # Randomly select top_n meals
    recommended = random.sample(filtered, min(top_n, len(filtered))) if filtered else []
    
    return recommended

# Example usage
if __name__ == "__main__":
    diet = "Protein-Rich"
    meal = "breakfast"
    calories = 250

    recommended_list = recommend_meals(diet, meal, max_calories=calories)
    print(f"Recommended {meal} meals for {diet} diet (≤ {calories} cal):")
    for m in recommended_list:
        print(f"- {m['meal']} ({m['calories']} cal)")
