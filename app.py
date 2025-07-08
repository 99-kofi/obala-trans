
from flask import Flask, request, jsonify
from model_utils import translate_to_french

app = Flask(__name__)

@app.route("/")
def home():
    return "🔥 OBALA French Translator is Live!"

@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()
    english_text = data.get("text", "")
    french_text = translate_to_french(english_text)
    return jsonify({"french": french_text})

if __name__ == "__main__":
    app.run(debug=True)
