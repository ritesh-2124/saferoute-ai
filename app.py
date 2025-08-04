from flask import Flask, request, jsonify
from vertexai.generative_models import GenerativeModel
import vertexai

app = Flask(__name__)

# Initialize Vertex AI with your project and region
vertexai.init(project="saferoute-ai-467711", location="us-central1")

# Load the Gemini model once during startup
try:
    model = GenerativeModel("gemini-2.5-pro")
    print("Gemini model loaded successfully.")
except Exception as e:
    print("Model loading failed:", e)
    model = None

@app.route('/ask', methods=['POST'])
def ask_safety():
    if not model:
        return jsonify({"error": "Model not available"}), 500

    data = request.get_json()
    question = data.get('question')

    if not question:
        return jsonify({"error": "No question provided"}), 400

    try:
        # Single-turn request (no chat history)
        response = model.generate_content(question)
        return jsonify({"response": response.text})
    except Exception as e:
        print("Error during response generation:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
