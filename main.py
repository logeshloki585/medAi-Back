from flask import Flask, request, jsonify
from flask_cors import CORS
from faceDetection import recognize_person_base64
import json

app = Flask(__name__)
CORS(app)

try:
    with open('data.json', 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    data = {}

@app.route('/register', methods=['POST'])
def register_data():
    data_id = request.json.get('id')
    data_content = request.json.get('content')
    print(data_content)
    data[data_id] = data_content

    # Save data to the JSON file
    with open('data.json', 'w') as file:
        json.dump(data, file)

    return jsonify({"message": "Data registered successfully"})

@app.route('/fetchdata/<int:data_id>', methods=['GET'])
def fetch_data(data_id):
    if data_id in data:
        return jsonify({"id": data_id, "data": data[data_id]})
    else:
        return jsonify({"message": "Data not found"}, 404)

@app.route('/verify', methods=['POST'])
def verify_face():
    try:
        data = request.get_json()
        image_data = data.get('image')
        if image_data:
            result = recognize_person_base64(image_data, 'db')
            return jsonify({'status': result})
        else:
            return jsonify({'status': 'Person does not exist'})
    except Exception as e:
        return jsonify({'status': str(e)})

if __name__ == '__main__':
    app.run(host='localhost', port=4000)
