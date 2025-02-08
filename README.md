# Library_Management

A web-based library management system built with Flask and MySQL that handles book management, student registrations, and book return tracking.

## Project Structure

- app.py: Flask backend with API endpoints and database connections
- index.html: Frontend interface built with HTML, Bootstrap, and JavaScript
- README.md: Project documentation

## Features

### 1. Book Management
- Add new books with:
  - Title (required)
  - Author (required)
  - Genre
  - Published date
- View complete book list in real-time

### 2. Student Registration
- Register students with:
  - Name (required)
  - Roll number (required)
  - Course selection (COE, ECE, ENC, COPC)
  - Assigned book ID
- View registered students list

### 3. Book Return Status Tracking
- Update book return status:
  - Student roll number
  - Book ID
  - Return status (Returned/Not Returned)
- View all return status records

## Technical Implementation

### Backend (app.py)
```python
# Key endpoints
@app.route('/books', methods=['GET', 'POST'])
@app.route('/students', methods=['GET', 'POST'])
@app.route('/status', methods=['GET', 'POST', 'PUT'])
```

### Frontend (templates/index.html)
- Bootstrap 4.5.2 for styling
- Vanilla JavaScript for:
  - Form handling
  - Dynamic content updates
  - API interactions

### Database Structure
```sql
books:
  - id
  - title
  - author
  - genre
  - published_date

students:
  - id
  - name
  - rollnumber
  - course
  - book_id

ret_status:
  - id
  - rollnumber
  - book_id
  - returned_status
```

## Setup Instructions

1. Configure MySQL database:
```python
mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='library_management'
)
```

2. Run Flask application:
```bash
python app.py
```

3. Access web interface at `http://localhost:5000`

## License

This project is licensed under the MIT License.