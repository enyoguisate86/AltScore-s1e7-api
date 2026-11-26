from flask import Flask, jsonify

import random


# map of system names to their codes
map_system = {
    "navigation": "NAV-01",
    "communications": "COM-02",
    "life_support": "LIFE-03",
    "engines": "ENG-04",
    "deflector_shield": "SHLD-05"
}

# select a random damaged system
damaged_system = None

def getStatus():
    global damaged_system
    if damaged_system is None:
        damaged_system = random.choice(list(map_system.keys()))
    return damaged_system

# initialize Flask app
app = Flask(__name__)

# get /status
@app.route('/status', methods=['GET'])
def status():
    return jsonify({"damaged_system": getStatus()}) 

# get /repair-bay
@app.route('/repair-bay', methods=['GET'])
def repair_bay():
    code = map_system[getStatus()]
    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>Repair</title>
</head>
<body>
<div class="anchor-point">{code}</div>
</body>
</html>"""
    return html_content

# post /teapot
@app.route('/teapot', methods=['POST'])
def teapot():
    return jsonify({"message": "I'm a teapot"}), 418

if __name__ == "__main__":
    app.run(port=5000)
    