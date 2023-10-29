from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def connect_db():
    return sqlite3.connect('database.db')

def init_db():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT, date TEXT, responsible TEXT, observations TEXT, status TEXT)''')
    conn.commit()
    conn.close()

init_db()  # Cria a tabela se ela não existir

@app.route('/', methods=['GET'])
def index():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)

@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    if request.method == 'POST':
        task = request.form['task']
        date = request.form['date']
        responsible = request.form['responsible']
        observations = request.form['observations']
        status = request.form['status']

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tasks (task, date, responsible, observations, status) VALUES (?, ?, ?, ?, ?)", (task, date, responsible, observations, status))
        conn.commit()
        conn.close()
        
        return redirect(url_for('index'))

    return render_template('tasks.html')

if __name__ == '__main__':
    app.run(debug=True)
