from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

tasks = [
    {"id": 1, "task": "Buy groceries"},
    {"id": 2, "task": "Walk the dog"},
    {"id": 3, "task": "Prepare dinner"}
]

@app.route('/tasks', methods=['GET','OPTIONS'])
def test_endpoint():
    return jsonify(tasks), 200

@app.route('/tasks', methods=['POST', 'OPTIONS'])
def create_task():
    return request.get_json()

@app.route('/tasks', methods=['DELETE', 'OPTIONS'])
def delete_task():
    return request.get_json()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

