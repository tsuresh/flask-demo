from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# MySQL configuration
db_config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'port': '8889',
    'database': 'flask'
}

def get_db_connection():
    conn = mysql.connector.connect(**db_config)
    return conn

@app.route('/')
def index():
    return 'Welcome to the Flask MySQL app!'

@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(users)

@app.route('/user', methods=['POST'])
def add_user():
    new_user = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO users (name, email) VALUES (%s, %s)',
        (new_user['name'], new_user['email'])
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'User added successfully!'}), 201

if __name__ == '__main__':
    app.run(debug=True)
