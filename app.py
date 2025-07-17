from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///docky.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Ensure uploads directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    filename = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

db.create_all()

@app.route('/', methods=['GET', 'POST'])
def user_dashboard():
    if request.method == 'POST':
        name = request.form['name']
        file = request.files['file']
        if name and file:
            filename = file.filename
            timestamp = datetime.now()
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            submission = Submission(name=name, filename=filename, timestamp=timestamp)
            db.session.add(submission)
            db.session.commit()
            return redirect(url_for('user_dashboard'))
    return render_template('user.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/admin')
def admin_dashboard():
    submissions = Submission.query.order_by(Submission.timestamp.desc()).all()
    return render_template('admin.html', submissions=submissions)

if __name__ == '__main__':
    app.run(debug=True)
