from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

def check_password_strength(password):
    strength = 0
    feedback = []

    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Use at least 8 characters.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Include an uppercase letter.")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Include a lowercase letter.")

    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("Include a number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Include a special character.")

    return strength, feedback

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check():
    try:
        data = request.get_json()
        password = data.get("password", "")
        strength, feedback = check_password_strength(password)
        return jsonify({"strength": strength, "feedback": feedback})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
