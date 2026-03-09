import os
from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# 🔑 API key from environment variable (do NOT hardcode!)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")

def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    question = data.get("question")
    length = data.get("length", "medium")  # short/medium/long

    # Map length to max_tokens
    max_tokens = 100
    if length == "medium":
        max_tokens = 200
    elif length == "long":
        max_tokens = 400

    try:
        # Latest OpenAI API
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful study buddy that explains answers clearly for students."},
                {"role": "user", "content": question}
            ],
            max_tokens=max_tokens
        )
        answer = response.choices[0].message.content
    except Exception as e:
        answer = f"Error: {str(e)}"

    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
    