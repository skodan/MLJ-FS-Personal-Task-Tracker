from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow React to connect

@app.route('/')
def home():
    return jsonify({"message": "Task Tracker API Running!"})

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = [
        {"id": 1, "title": "Learn Flask", "completed": False},
        {"id": 2, "title": "Connect to React", "completed": False}
    ]
    return jsonify(tasks)

if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(debug=True, port=5000)