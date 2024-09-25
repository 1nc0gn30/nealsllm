from flask import Flask, request, jsonify
from flask_cors import CORS
import ollama  # Import the Ollama Python package

app = Flask(__name__)
CORS(app)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt')

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    try:
        # Use Ollama's Python API to generate a response
        result = ollama.chat(model='llama2', messages=[{'role': 'user', 'content': prompt}])
        response = result['message']['content']
        return jsonify({"response": response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
