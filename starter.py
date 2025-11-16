from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'message': 'Hello World'
    }), 200

@app.route('/items', methods=['GET'])
def read_items():
    return jsonify({
        'message': 'Hello, World!'
    }), 200

@app.route('/post', methods=['POST'])
def post_items():
    return jsonify({
        'message': 'This is a post request!'
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)