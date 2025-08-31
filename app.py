from flask import Flask, jsonify
import json

app = Flask(__name__)

# API route
@app.route('/api', methods=['GET'])
def get_data():
    try:
        # Read data from backend file
        with open("data.json", "r") as file:
            data = json.load(file)
        return jsonify(data)  # Return as JSON
    except FileNotFoundError:
        return jsonify({"error": "Data file not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON format in file"}), 500

if __name__ == '__main__':
    app.run(debug=True)

