from flask import Flask, render_template, request, redirect, url_for, send_from_directory, session, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///docky.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'change_this_secret_key'  # Needed for session

db = SQLAlchemy(app)

# Ensure uploads directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    filename = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# Create tables within app context
with app.app_context():
    db.create_all()

@app.route('/', methods=['GET'])
def upload_page():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
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
        return ('', 200)
    return ('Missing data', 400)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/dashboard', methods=['GET', 'POST'])
def user_dashboard():
    if 'dashboard_auth' not in session:
        if request.method == 'POST':
            password = request.form.get('password')
            if password == 'Nuvai$123':
                session['dashboard_auth'] = True
                return redirect(url_for('user_dashboard'))
            else:
                return render_template('dashboard_login.html', error='Incorrect password')
        return render_template('dashboard_login.html')
    return render_template('user.html')

@app.route('/dashboard/logout')
def dashboard_logout():
    session.pop('dashboard_auth', None)
    return redirect(url_for('user_dashboard'))

@app.route('/admin', methods=['GET', 'POST'])
def admin_dashboard():
    if 'admin_auth' not in session:
        if request.method == 'POST':
            password = request.form.get('password')
            if password == 'Nuvai$123':
                session['admin_auth'] = True
                return redirect(url_for('admin_dashboard'))
            else:
                return render_template('admin_login.html', error='Incorrect password')
        return render_template('admin_login.html')
    submissions = Submission.query.order_by(Submission.timestamp.desc()).all()
    return render_template('admin.html', submissions=submissions)

@app.route('/admin/logout')
def admin_logout():
    session.pop('admin_auth', None)
    return redirect(url_for('admin_dashboard'))

@app.route('/submissions')
def submissions_api():
    submissions = Submission.query.order_by(Submission.timestamp.desc()).all()
    return [{
        'name': s.name,
        'filename': s.filename,
        'timestamp': s.timestamp.isoformat()
    } for s in submissions]

@app.route('/delete/<filename>', methods=['DELETE'])
def delete_file(filename):
    if 'dashboard_auth' not in session and 'admin_auth' not in session:
        return abort(403)
    submission = Submission.query.filter_by(filename=filename).first()
    if not submission:
        return abort(404)
    try:
        db.session.delete(submission)
        db.session.commit()
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        if os.path.exists(filepath):
            os.remove(filepath)
        return ('', 200)
    except Exception as e:
        return abort(500)

if __name__ == '__main__':
    app.run(debug=True)
