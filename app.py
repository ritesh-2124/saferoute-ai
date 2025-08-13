from flask import Flask, request, jsonify ,render_template
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
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/ask', methods=['POST'])
def ask_safety():
    if not model:
        return jsonify({"error": "Model not available"}), 500

    data = request.get_json()
    question = data.get('question')
    latitude = data.get('latitude')
    longitude = data.get('longitude')

    print("Received question:", question , latitude, longitude)
    if not question:
        return jsonify({"error": "No question provided"}), 400
        # If location is provided, append it to the prompt
    if latitude and longitude:
        location_info = f"The user is currently at coordinates {latitude}, {longitude}. " \
                        "Provide safety tips or advice relevant to this location."
        question = f"{question}\n\n{location_info}"

    try:
        # Single-turn request (no chat history)
        prompt = f"Answer briefly and clearly in under 3 sentences is it safe for women. {question}"
        response = model.generate_content(prompt)

        return jsonify({"response": response.text})
    except Exception as e:
        print("Error during response generation:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)