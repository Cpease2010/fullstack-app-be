from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

tasks = [
    {"id": 1, "task": "Buy groceries"},
    {"id": 2, "task": "Walk the dog"},
    {"id": 3, "task": "Prepare dinner"}
]

@app.route('/tasks', methods=['GET'])
def test_endpoint():
    return jsonify(tasks), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

