import json
from typing import List, Dict
from ai_recommender import score_meals  # new AI function
from diet_rules import validate_meal_plan_prolog  # your Prolog validator

# Load meal data
with open("meal_data.json") as f:
    meal_data = json.load(f)

def get_meals(diet_type: str, meal_type: str) -> List[Dict]:
    if diet_type not in meal_data:
        return []
    return [meal for meal in meal_data[diet_type] if meal_type in meal['tags']]

def get_recommended_meals(diet_type: str, meal_type: str, user_preferences: dict) -> List[Dict]:
    """Returns AI-ranked meals filtered by Prolog rules."""
    meals = get_meals(diet_type, meal_type)
    scored_meals = score_meals(meals, user_preferences)  # AI scores/ranks
    # Optionally validate each meal plan
    recommended = [meal for meal in scored_meals if validate_meal_plan_prolog([meal])]
    return recommended
