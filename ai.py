# from flask import Flask, request, jsonify
# import openai
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)  # Allow frontend requests

# openai.api_key = "your_openai_api_key"

# @app.route("/voice-assistant", methods=["POST"])
# def voice_assistant():
#     data = request.json
#     user_query = data.get("query", "")

#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[{"role": "user", "content": user_query}]
#     )

#     reply = response["choices"][0]["message"]["content"].strip()
#     return jsonify({"reply": reply})

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000, debug=True)
from flask import Flask, request, jsonify
import openai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend requests

openai.api_key = "your_openai_api_key"

@app.route("/voice-assistant", methods=["POST"])
def voice_assistant():
    data = request.json
    user_query = data.get("query", "")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_query}]
        )

        reply = response["choices"][0]["message"]["content"].strip()
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"reply": "Sorry, I couldn't process your request right now."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
