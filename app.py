from flask import Flask, request, jsonify
from diet_service import get_meals_by_tag, validate_meal_plan

app = Flask(__name__)

@app.route('/')
def home():
    return "Diet API is running!"

# Get meals by tag or category
@app.route('/meals', methods=['GET'])
def meals():
    tag = request.args.get('tag')  
    if not tag:
        return jsonify({"error": "Please provide a tag parameter"}), 400
    meals_list = get_meals_by_tag(tag)
    return jsonify({"tag": tag, "meals": meals_list})

# Validate a meal plan
@app.route('/validate', methods=['POST'])
def validate():
    data = request.get_json()
    if not data or "meal_plan" not in data:
        return jsonify({"error": "Send JSON with 'meal_plan' list"}), 400
    meal_plan = data["meal_plan"]
    is_valid, message = validate_meal_plan(meal_plan)
    return jsonify({"valid": is_valid, "message": message})

if __name__ == '__main__':
    app.run(debug=True)
