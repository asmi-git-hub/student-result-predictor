from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Student Result Predictor</title>
</head>
<body>
    <h1>Student Result Predictor</h1>

    <form method="POST">
        <label>Study Hours:</label>
        <input type="number" name="hours" step="0.1" required><br><br>

        <label>Attendance (%):</label>
        <input type="number" name="attendance" step="0.1" required><br><br>

        <label>Internal Marks:</label>
        <input type="number" name="internal" step="0.1" required><br><br>

        <button type="submit">Predict</button>
    </form>

    {% if result %}
        <h2>Prediction: {{ result }}</h2>
        <p>Model Version: 2.0</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def predict():
    result = None

    if request.method == "POST":
        hours = float(request.form["hours"])
        attendance = float(request.form["attendance"])
        internal = float(request.form["internal"])

        # Simple prediction logic
        if hours >= 2 and attendance >= 75 and internal >= 40:
            result = "PASS"
        else:
            result = "FAIL"

    return render_template_string(HTML, result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)