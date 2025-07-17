# Docky

A minimal Flask web app for document uploads and admin review.

## Features
- User dashboard: Upload your name and a document
- Admin dashboard: View all submissions (name, document link, timestamp)
- Uses Flask + Flask-SQLAlchemy + SQLite (no MySQL)
- Stores uploads in /uploads
- Ready for local use and Render deployment

## Setup & Run Locally
1. **Clone the repo:**
   ```
   git clone https://github.com/THARUNKUMAR7379/Docky.git
   cd Docky
   ```
2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```
3. **Run the app:**
   ```
   python app.py
   # or
   python3 app.py
   ```
4. **Visit:**
   - User dashboard: http://localhost:5000/
   - Admin dashboard: http://localhost:5000/admin

## Deploy on Render
1. **Create a new Web Service** on [Render](https://render.com/)
2. **Set build & start commands:**
   - Build command: `pip install -r requirements.txt`
   - Start command: `gunicorn app:app`
3. **Set environment:**
   - Python 3.7+
   - Ensure `uploads/` folder is created (the app will auto-create it)

## File Structure
- `app.py` — Main Flask app
- `templates/user.html` — User upload form
- `templates/admin.html` — Admin dashboard
- `uploads/` — Uploaded documents

## Notes
- No authentication (for demo simplicity)
- Only Flask + Flask-SQLAlchemy used
- SQLite DB auto-creates on first run