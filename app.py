# from flask import Flask, request, jsonify, render_template
# import mysql.connector

# app = Flask(__name__)

# def get_db_connection():
#     return mysql.connector.connect(
#         host='localhost',
#         user='root',
#         password='root',
#         database='library_management'
#     )

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/books', methods=['GET'])
# def get_books():
#     connection = get_db_connection()
#     cursor = connection.cursor(dictionary=True)
#     cursor.execute('SELECT * FROM books')
#     books = cursor.fetchall()
#     cursor.close()
#     connection.close()
#     return jsonify(books)

# @app.route('/books', methods=['POST'])
# # def add_book():
# #     new_book = request.json
# #     connection = get_db_connection()
# #     cursor = connection.cursor()
# #     cursor.execute('INSERT INTO books (title, author, genre, published_date) VALUES (%s, %s, %s, %s)',
# #                    (new_book['title'], new_book['author'], new_book['genre'], new_book['published_date']))
# #     connection.commit()
# #     new_book_id = cursor.lastrowid
# #     cursor.close()
# #     connection.close()
# #     return jsonify({**new_book, 'id': new_book_id}), 201



# @app.route('/books', methods=['POST'])
# def add_book():
#     try:
#         new_book = request.json
#         connection = get_db_connection()
#         cursor = connection.cursor()

#         cursor.execute('INSERT INTO books (title, author, genre, published_date) VALUES (%s, %s, %s, %s)',
#                        (new_book['title'], new_book['author'], new_book['genre'], new_book['published_date']))
#         connection.commit()
#         new_book_id = cursor.lastrowid  # Get the newly inserted book ID

#         cursor.close()
#         connection.close()

#         return jsonify({'id': new_book_id, **new_book}), 201  # Return new book ID along with data
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500



# @app.route('/students', methods=['GET'])
# def get_students():
#     connection = get_db_connection()
#     cursor = connection.cursor(dictionary=True)
#     cursor.execute('SELECT * FROM students')
#     students = cursor.fetchall()
#     cursor.close()
#     connection.close()
#     return jsonify(students)



# @app.route('/status', methods=['GET'])
# def get_status():
#     connection = get_db_connection()
#     cursor = connection.cursor(dictionary=True)
#     cursor.execute('SELECT * FROM ret_status')
#     status_list = cursor.fetchall()
#     cursor.close()
#     connection.close()
#     return jsonify(status_list)

# @app.route('/status', methods=['POST'])
# def add_status():
#     new_status = request.json
#     connection = get_db_connection()
#     cursor = connection.cursor()
#     cursor.execute('INSERT INTO ret_status (rollnumber, book_id, returned_status) VALUES (%s, %s, %s)',
#                    (new_status['rollnumber'], new_status['book_id'], new_status['returned_status']))
#     connection.commit()
#     new_status_id = cursor.lastrowid
#     cursor.close()
#     connection.close()
#     return jsonify({**new_status, 'id': new_status_id}), 201

# @app.route('/status/<int:status_id>', methods=['PUT'])
# def update_status(status_id):
#     updated_status = request.json
#     connection = get_db_connection()
#     cursor = connection.cursor()
#     cursor.execute('UPDATE ret_status SET returned_status = %s WHERE id = %s',
#                    (updated_status['returned_status'], status_id))
#     connection.commit()
#     cursor.close()
#     connection.close()
#     return jsonify({"message": "Status updated successfully"}), 200

# if __name__ == '__main__':
#     app.run(debug=True)







# @app.route('/students', methods=['POST'])
# def add_student():
#     try:
#         new_student = request.json
#         connection = get_db_connection()
#         cursor = connection.cursor()

#         cursor.execute('INSERT INTO students (name, age, course) VALUES (%s, %s, %s)',
#                        (new_student['name'], new_student['age'], new_student['course']))
#         connection.commit()
#         new_student_id = cursor.lastrowid

#         cursor.close()
#         connection.close()

#         return jsonify({**new_student, 'id': new_student_id}), 201
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# # Route to fetch all students
# @app.route('/students', methods=['GET'])
# def get_students():
#     connection = get_db_connection()
#     cursor = connection.cursor(dictionary=True)

#     cursor.execute('SELECT * FROM students')
#     students = cursor.fetchall()

#     cursor.close()
#     connection.close()

#     return jsonify(students)


# # Route to add a status
# @app.route('/status', methods=['POST'])
# def add_status():
#     try:
#         new_status = request.json
#         connection = get_db_connection()
#         cursor = connection.cursor()

#         cursor.execute('INSERT INTO status (student_id, status_text) VALUES (%s, %s)',
#                        (new_status['student_id'], new_status['status_text']))
#         connection.commit()
#         new_status_id = cursor.lastrowid

#         cursor.close()
#         connection.close()

#         return jsonify({**new_status, 'id': new_status_id}), 201
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# # Route to fetch all statuses
# @app.route('/status', methods=['GET'])
# def get_status():
#     connection = get_db_connection()
#     cursor = connection.cursor(dictionary=True)

#     cursor.execute('SELECT * FROM status')
#     statuses = cursor.fetchall()

#     cursor.close()
#     connection.close()

#     return jsonify(statuses)





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
        print(students)  # Debugging
        cursor.close()
        connection.close()
        return jsonify(students), 200
    except Exception as e:
        print(f"Error: {e}")  # Log the error
        return jsonify({"error": str(e)}), 500
    



@app.route('/students', methods=['POST'])
def add_student():
    try:
        new_student = request.json
        print("Received Data:", new_student)  # Log the incoming data
        
        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute(
            'INSERT INTO students (name, age, course) VALUES (%s, %s, %s)',
            (new_student['name'], new_student['age'], new_student['course'])
        )
        connection.commit()
        new_student_id = cursor.lastrowid

        cursor.close()
        connection.close()

        return jsonify({**new_student, 'id': new_student_id}), 201
    except Exception as e:
        print("Error in /students endpoint:", str(e))
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
