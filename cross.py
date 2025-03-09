from flask import Flask, render_template_string
import time
import random
from datetime import datetime

app = Flask(__name__)

# Define the result pattern
results = [
    "SMALL 0 RED", "SMALL 3 GREEN", "BIG 7 GREEN", "SMALL 1 GREEN",
    "BIG 6 RED", "BIG 8 RED", "BIG 9 GREEN", "SMALL 4 RED",
    "SMALL 2 RED", "BIG 5 GREEN", "SMALL 3 GREEN", "BIG 7 GREEN",
    "SMALL 1 GREEN", "SMALL 1 GREEN", "SMALL 3 GREEN", "BIG 7 GREEN",
    "BIG 7 GREEN", "BIG 9 GREEN", "SMALL 3 GREEN", "BIG 7 GREEN",
    "SMALL 1 GREEN", "SMALL 1 GREEN", "SMALL 3 GREEN", "BIG 7 GREEN",
    "BIG 7 GREEN", "BIG 9 GREEN"
]

# Period calculation based on UTC time
def calculate_period_number():
    utc_now = datetime.utcnow()
    total_minutes = utc_now.hour * 60 + utc_now.minute
    return f"{utc_now.strftime('%Y%m%d')}1000{10001 + total_minutes}"

# Get a random result
def get_random_result():
    return random.choice(results)

# HTML template for displaying results
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Prediction Results</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; padding: 20px; }
        .result-box { border: 2px solid #333; padding: 20px; display: inline-block; }
        .green { color: green; }
        .red { color: red; }
    </style>
</head>
<body>
    <h1>PANDA MODS PREDICTION</h1>
    <div class="result-box">
        <h2>Period: {{ period }}</h2>
        <h3 class="{{ color }}">Result: {{ result }}</h3>
    </div>
    <br><br>
    <button onclick="location.reload()">Refresh</button>
</body>
</html>
"""

@app.route('/')
def home():
    period = calculate_period_number()
    result = get_random_result()
    color = "green" if "GREEN" in result else "red"
    return render_template_string(HTML_TEMPLATE, period=period, result=result, color=color)

if __name__ == '__main__':
    app.run(debug=True)
