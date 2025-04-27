from flask import Flask, render_template, request, jsonify
from chatbot import get_response

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_text = request.json.get("msg")
    print("User said:", user_text)  # Debug
    response = get_response(user_text)
    print("Bot replied:", response)  # Debug
    return jsonify(reply=response)

if __name__ == "__main__":
    app.run(debug=True)
