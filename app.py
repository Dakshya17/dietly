from flask import Flask, request, jsonify
from diet_service import get_recommended_meals

app = Flask(__name__)

@app.route('/')
def home():
    return "Diet API running!"

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    if not data or "diet_type" not in data or "meal_type" not in data:
        return jsonify({"error": "Send 'diet_type' and 'meal_type'"}), 400
    diet_type = data["diet_type"]
    meal_type = data["meal_type"]
    user_preferences = data.get("preferences", {})  # e.g., {"goal": "Protein-Rich"}
    meals = get_recommended_meals(diet_type, meal_type, user_preferences)
    return jsonify({"recommended_meals": meals})

if __name__ == "__main__":
    app.run(debug=True)
