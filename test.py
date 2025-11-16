from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username != 'admin' or password != 'secret':
        return jsonify({
            'error': 'Invalid username or password',
        }), 401
    else:
        return jsonify({
            'message': 'Hello ' + username + ', you have successfully logged in.',
        }), 200


if __name__ == '__main__':
    app.run(debug=True)
