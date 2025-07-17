from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask_mysqldb import MySQL
import os
from datetime import datetime

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''  # Set your MySQL root password here
app.config['MYSQL_DB'] = 'dockydb'

mysql = MySQL(app)

# Ensure uploads directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def user_dashboard():
    if request.method == 'POST':
        name = request.form['name']
        file = request.files['file']
        if name and file:
            filename = file.filename
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            cur = mysql.connection.cursor()
            cur.execute('INSERT INTO submissions (name, filename, timestamp) VALUES (%s, %s, %s)', (name, filename, timestamp))
            mysql.connection.commit()
            cur.close()
            return redirect(url_for('user_dashboard'))
    return render_template('user.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/admin')
def admin_dashboard():
    cur = mysql.connection.cursor()
    cur.execute('SELECT name, filename, timestamp FROM submissions ORDER BY timestamp DESC')
    submissions = cur.fetchall()
    cur.close()
    return render_template('admin.html', submissions=submissions)

if __name__ == '__main__':
    app.run(debug=True)
