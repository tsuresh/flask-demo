from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory array to act as our database
items = []

@app.route('/items', methods=['POST'])
def create_item():
    """Create a new item."""
    data = request.get_json()
    item = {
        'id': len(items) + 1,
        'name': data['name'],
        'description': data.get('description', '')
    }
    items.append(item)
    return jsonify(item), 201

@app.route('/items', methods=['GET'])
def read_items():
    """Read all items."""
    return jsonify(items), 200

@app.route('/items/<int:item_id>', methods=['GET'])
def read_item(item_id):
    """Read a single item."""
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({'error': 'Item not found'}), 404
    return jsonify(item), 200

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    """Update an existing item."""
    data = request.get_json()
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({'error': 'Item not found'}), 404
    
    item['name'] = data.get('name', item['name'])
    item['description'] = data.get('description', item['description'])
    return jsonify(item), 200

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    """Delete an item."""
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({'message': 'Item deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)
