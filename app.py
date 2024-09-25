from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt')

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    try:
        # Call the Ollama model using subprocess
        result = subprocess.run(
            ['ollama', 'run', 'llama3.1', prompt],
            capture_output=True, text=True, check=True
        )

        response = result.stdout.strip()
        return jsonify({"response": response})

    except subprocess.CalledProcessError as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

