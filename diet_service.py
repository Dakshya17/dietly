import json
from typing import List, Dict

# Load JSON
with open("meal_data.json") as f:
    meal_data = json.load(f)

# Function to get meals for a specific diet and meal type
def get_meals(diet_type: str, meal_type: str) -> List[Dict]:
    """Return meals for a specific diet and meal type."""
    if diet_type not in meal_data:
        return []
    return [meal for meal in meal_data[diet_type] if meal_type in meal['tags']]

# Example usage
if __name__ == "__main__":
    protein_breakfasts = get_meals("Protein-Rich", "breakfast")
    for meal in protein_breakfasts:
        print(meal)
