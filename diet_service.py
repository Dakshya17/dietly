import json

# Load the meals data from the JSON file
with open("../meal_data.json", "r") as file:
    meals_data = json.load(file)

# Function to get meals for a diet
def get_meals(diet_name):
    return meals_data.get(diet_name, [])

# Example: test it
if __name__ == "__main__":
    diet = "Anti-Inflammatory"  # Change this to test other diets
    meals = get_meals(diet)
    print(f"Meals for {diet}:")
    for m in meals:
        print("-", m["meal"], "|", m["calories"], "calories |", ", ".join(m["tags"]))
