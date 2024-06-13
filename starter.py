from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/items', methods=['GET'])
def read_items():
    """Read all items."""
    return jsonify({
        'message': 'Hello, World!'
    }), 200

if __name__ == '__main__':
    app.run(debug=True)