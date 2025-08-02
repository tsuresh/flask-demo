from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/login', methods=['POST'])
def login():
    """User login."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # add your own logic right here
    if username != 'admin' or password != 'secret':
        return jsonify({
            'error': 'Invalid username or password',
        }), 401

    return jsonify({
        'message': 'Hello ' + username + ', you have successfully logged in.',
    }), 201

if __name__ == '__main__':
    app.run(debug=True)
