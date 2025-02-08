from flask import Flask, request, jsonify, render_template
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='library_management'
    )

@app.route('/')
def index():
    return render_template('index.html')

# Books Routes
@app.route('/books', methods=['GET'])
def get_books():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(books)

@app.route('/books', methods=['POST'])
def add_book():
    try:
        new_book = request.json
        connection = get_db_connection()
        cursor = connection.cursor()
        
        cursor.execute('INSERT INTO books (title, author, genre, published_date) VALUES (%s, %s, %s, %s)',
                       (new_book['title'], new_book['author'], new_book['genre'], new_book['published_date']))
        connection.commit()
        new_book_id = cursor.lastrowid

        cursor.close()
        connection.close()
        
        return jsonify({'id': new_book_id, **new_book}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/students', methods=['GET'])
def get_students():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute('SELECT * FROM students')
        students = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(students), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/students', methods=['POST'])
def add_student():
    try:
        new_student = request.json
        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute(
            'INSERT INTO students (name, rollnumber, course, book_id) VALUES (%s, %s, %s, %s)',
            (new_student['name'], new_student['rollnumber'], new_student['course'], new_student.get('book_id'))
        )
        connection.commit()
        new_student_id = cursor.lastrowid

        cursor.close()
        connection.close()

        return jsonify({**new_student, 'id': new_student_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Status Routes
@app.route('/status', methods=['GET'])
def get_status():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM ret_status')
    status_list = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(status_list)

@app.route('/status', methods=['POST'])
def add_status():
    try:
        new_status = request.json
        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute('INSERT INTO ret_status (rollnumber, book_id, returned_status) VALUES (%s, %s, %s)',
                       (new_status['rollnumber'], new_status['book_id'], new_status['returned_status']))
        connection.commit()
        new_status_id = cursor.lastrowid

        cursor.close()
        connection.close()
        
        return jsonify({**new_status, 'id': new_status_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/status/<int:status_id>', methods=['PUT'])
def update_status(status_id):
    try:
        updated_status = request.json
        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute('UPDATE ret_status SET returned_status = %s WHERE id = %s',
                       (updated_status['returned_status'], status_id))
        connection.commit()
        
        cursor.close()
        connection.close()
        
        return jsonify({"message": "Status updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)