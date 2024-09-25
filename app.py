from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

# Some random useful facts
FACTS = [
    "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible.",
    "Octopuses have three hearts and blue blood.",
    "Bananas are berries, but strawberries aren't.",
    "An octopus has nine brains—one central brain and one in each arm.",
    "Sharks are older than trees—they've been around for over 400 million years.",
]

@app.route('/random-fact', methods=['GET'])
def get_random_fact():
    """Return a random fact."""
    fact = random.choice(FACTS)
    return jsonify({"fact": fact})

@app.route('/convert-temp', methods=['GET'])
def convert_temperature():
    """Convert temperature between Celsius and Fahrenheit."""
    temp = request.args.get('temp', type=float)
    unit = request.args.get('unit')  # 'C' for Celsius or 'F' for Fahrenheit

    if unit == 'C':
        # Convert Celsius to Fahrenheit
        converted = (temp * 9/5) + 32
        return jsonify({"original": f"{temp}°C", "converted": f"{converted}°F"})
    elif unit == 'F':
        # Convert Fahrenheit to Celsius
        converted = (temp - 32) * 5/9
        return jsonify({"original": f"{temp}°F", "converted": f"{converted}°C"})
    else:
        return jsonify({"error": "Invalid unit, must be 'C' or 'F'"}), 400

@app.route('/math', methods=['GET'])
def perform_math():
    """Perform basic math operations (add, subtract, multiply, divide)."""
    num1 = request.args.get('num1', type=float)
    num2 = request.args.get('num2', type=float)
    operation = request.args.get('operation')  # 'add', 'subtract', 'multiply', 'divide'

    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return jsonify({"error": "Cannot divide by zero"}), 400
        result = num1 / num2
    else:
        return jsonify({"error": "Invalid operation. Must be add, subtract, multiply, or divide."}), 400

    return jsonify({"num1": num1, "num2": num2, "operation": operation, "result": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
