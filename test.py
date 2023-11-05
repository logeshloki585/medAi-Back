from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from medBot import _getBot

app = Flask(__name__)
CORS(app)


@app.route('/chat', methods=['POST'])
def verify_face():
    body = request.get_json()
    response=_getBot(body['user'])
    response = {"bot":response}
    print(response)
    return response

if __name__ == '__main__':
    app.run(host="localhost", port=5000)

