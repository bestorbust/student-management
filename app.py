from flask import Flask, request, jsonify, render_template,redirect,url_for
import sqlite3

app = Flask(__name__)
def init_db:
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    std_id TEXT NOT NULL,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    subject1 INTEGER NOT NULL,
                    subject2 INTEGER NOT NULL,
                    subject3 INTEGER NOT NULL,
                    subject4 INTEGER NOT NULL,
                    subject5 INTEGER NOT NULL
                    )''')
    conn.commit()
    conn.close()    

@app.route('/')
def home():
    with sqlite3.connect('students.db') as conn:
        student = conn.execute('SELECT * FROM students').fetchall()
    return render_template('std.html', student=student)
@app.route('/add', methods=['POST'])
def add_student():
    std_id = request.form['std_id']
    name = request.form['name']
    age = int(request.form['age'])
    subject1 = int(request.form['subject1'])
    subject2 = int(request.form['subject2'])
    subject3 = int(request.form['subject3'])
    subject4 = int(request.form['subject4'])
    subject5 = int(request.form['subject5'])
    with sqlite3.connect('students.db') as conn:
        conn.execute('INSERT INTO students (std_id, name, age, subject1, subject2, subject3, subject4, subject5) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',(std_id, name, age, subject1, subject2, subject3, subject4, subject5))
    return redirect(url_for('home'))
@app.route('/update', methods=['POST'])
def update_student():
    std_id = request.form['std_id']
    name = request.form['name']
    age = int(request.form['age'])
    subject1 = int(request.form['subject1'])
    subject2 = int(request.form['subject2'])
    subject3 = int(request.form['subject3'])
    subject4 = int(request.form['subject4'])
    subject5 = int(request.form['subject5'])
    with sqlite3.connect('students.db') as conn:
        conn.execute('UPDATE students SET name=?, age=?, subject1=?, subject2=?, subject3=?, subject4=?, subject5=? WHERE std_id=?', (name, age, subject1, subject2, subject3, subject4, subject5, std_id))
    return 'Student updated successfully!'
@app.route('/delete', methods=['POST'])
def delete_student():
    std_id = request.form['std_id']
    with sqlite3.connect('students.db') as conn:
        conn.execute('DELETE FROM students WHERE std_id=?', (std_id,))
    return "Student deleted successfully!"

@app.route('/search', methods=['GET'])
def search_student():
    search_query = request.args.get('query', '')
    with sqlite3.connect('students.db') as conn:
        results = conn.execute('SELECT * FROM students WHERE std_id LIKE ? OR name LIKE ?', (f'%{search_query}%', f'%{search_query}%')).fetchall()
    return jsonify(results)
        
init_db() 
if __name__=='main':
    app.run(debug=True)