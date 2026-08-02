from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# Gemini API Key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_message = request.json.get("message", "")

        response = model.generate_content(user_message)

        return jsonify({
            "reply": response.text
        })

    except Exception as e:
        return jsonify({
            "reply": f"Error: {str(e)}"
        })

if __name__ == "__main__":
    app.run(debug=True)
