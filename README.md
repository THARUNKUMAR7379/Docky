# 🚀 Docky: Deep Dive & Deployment Guide

Hello, fellow developer! 👋 As a senior full-stack dev and technical writer, here's a complete analysis of your Docky Flask project, covering every file, how the app works, and a Render deployment walkthrough. Let's make it crystal clear and beginner-proof! ☑️

---

## 📂 File-by-file Analysis

### 1. `app.py` — The Backend Brain 🧠
**Purpose:**  
Main Flask app. Handles routing, database, file upload logic, and admin controls.

**Key Logic:**
- **Flask Setup & Config:**  
  Sets up Flask, SQLAlchemy, SQLite DB (`docky.db`), and the `uploads` folder.
- **Database Model:**  
  `Submission` model tracks:  
  - `name` (string)  
  - `filename` (string)  
  - `timestamp` (datetime)
- **Upload Route:**  
  - `/upload` (POST): Accepts name + file, saves the file to `/uploads`, logs record in DB.
  - Ensures uploads folder exists.
- **Serve Uploaded Files:**  
  - `/uploads/<filename>`: Lets anyone download files.
- **Admin Dashboard:**  
  - `/admin` (GET/POST): Shows all submissions (name, file, timestamp). Protected by a hardcoded password ("Nuvai$123").
- **Delete Files:**  
  - `/delete/<filename>` (DELETE): Removes DB record and file.
- **Session:**  
  Used for admin authentication (not for users).
- **APIs:**  
  `/submissions` and `/my_uploads` return JSON lists for frontend dashboards.

**Connections:**
- Uses templates for rendering (`admin.html`, `upload.html`).
- Connects with `/uploads` for file storage.
- DB stores all submission data.

**Improvements:**
- 🚩 **Security:**  
  - Use `werkzeug.utils.secure_filename()` to sanitize uploads.
  - Avoid hardcoded admin passwords; consider env variables.
- 🚩 **File Validation:**  
  - Limit file size and types (currently accepts anything).
- 🚩 **Error Handling:**  
  - More user-friendly messages on failure.
- 🚩 **Use upload.html naming consistently (currently called `user.html` in repo).**
- 🚩 **Logging:**  
  - Add logging for uploads, errors, and deletions.

---

### 2. `templates/user.html` — User Dashboard 🎨
**Purpose:**  
Front-end for users to upload their name and documents.

**Key Logic:**
- **Tailwind CSS:** Stylish, modern layout with light/dark mode toggle.
- **Form Functionality:**  
  - Search and sort files.
  - Preview files in a modal (supports images, video, PDF, TXT).
  - Download and delete files.
- **JS Logic:**  
  - Fetches submissions via `/submissions` API.
  - Handles upload, preview, deletion with fetch/XHR.

**Connections:**
- Calls backend for file actions.
- Renders data from `/submissions` API.

**Improvements:**
- 🚩 **Display upload form directly (currently only lists files).**
- 🚩 **Add drag-and-drop upload for UX.**
- 🚩 **Show upload progress/loading.**

---

### 3. `templates/admin.html` — Admin Dashboard 🛡️
**Purpose:**  
Front-end for admins to view, search, sort, and manage all submissions.

**Key Logic:**
- **Tailwind CSS:** Same modern look as user view.
- **Table View:**  
  - Shows preview, filename, uploader, timestamp, actions (download, preview, delete).
- **JS Logic:**  
  - Fetches all submissions via `/submissions`.
  - Handles file deletion, modal preview, search/sort.
- **Admin Access:**  
  - Requires login (via password in session).

**Connections:**
- Connected to `/admin` route and `/submissions` API.

**Improvements:**
- 🚩 **Pagination for large datasets.**
- 🚩 **More robust admin authentication (not just password in session).**
- 🚩 **Bulk delete/select.**

---

### 4. `/uploads` — File Storage 📁
**Purpose:**  
Holds all user-uploaded files.

**Key Logic:**
- All files are saved here via `file.save(filepath)` in `app.py`.
- Files are served directly by Flask (`send_from_directory`).

**Connections:**
- Referenced in `/uploads/<filename>` route in Flask.

**Improvements:**
- 🚩 **Check for duplicate filenames (could overwrite).**
- 🚩 **Clean up orphaned files (not in DB).**
- 🚩 **Add max file size check at Flask config level.**

---

### 5. `requirements.txt` — Dependencies 📦
```text
Flask
Flask-SQLAlchemy
Gunicorn 
```
**Purpose:**  
Lists Python packages needed for app and deployment.

**Connections:**
- For `pip install -r requirements.txt` before running or deploying.

**Improvements:**
- 🚩 **Pin package versions (e.g., Flask==3.0.0) for reliability.**
- 🚩 **Add any missing packages (e.g., python-dotenv if using env vars later).**

---

## 🔄 Complete Flow: From Upload to Admin View

1. **User Uploads a File:**
   - User enters their name and selects a file.
   - Form POSTs to `/upload`.
   - Flask saves the file in `/uploads`.
   - Entry is added to SQLite DB (`docky.db`): name, filename, timestamp.

2. **Data in SQLite:**
   - Table: `Submission`
   - Columns: `id`, `name`, `filename`, `timestamp`

3. **Admin Dashboard:**
   - Admin logs in via `/admin` (password-based).
   - Flask queries all submissions (`Submission.query.order_by(...)`).
   - Renders each with download link (`/uploads/<filename>`) and timestamp.
   - Can delete files (removes both DB entry and actual file from disk).

4. **File Saving:**
   - All uploaded files go to `/uploads`.
   - Download links use `/uploads/<filename>`.
   - Deletion removes both DB row and file.

---

## 🚀 Deploy to Render: Step-by-Step Guide

### 1️⃣ Prepare Your Repo

- Ensure all files are present:  
  `app.py`, `/templates`, `/uploads` (empty but exists), `requirements.txt`

- Optional: Add a `Procfile` for Gunicorn
  ```text
  web: gunicorn app:app
  ```

### 2️⃣ Create `render.yaml` (optional, for custom setup)
```yaml
services:
  - type: web
    name: docky
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn app:app
    disk:
      name: docky-uploads
      mountPath: uploads
      sizeGB: 1
```

### 3️⃣ Push to GitHub

```bash
git add .
git commit -m "Ready for render deploy"
git push origin main
```

### 4️⃣ Set Up on Render

- Go to [Render dashboard](https://dashboard.render.com/)
- Click **New Web Service**
- Connect your GitHub repo (`THARUNKUMAR7379/Docky`)
- Set **Build Command:**  
  ```bash
  pip install -r requirements.txt
  ```
- Set **Start Command:**  
  ```bash
  gunicorn app:app
  ```
- **Add a Persistent Disk** for `/uploads` (see render.yaml above)
- Confirm Python environment (Render auto-detects from requirements.txt)

### 5️⃣ Folder Structure Check

- `/uploads` must exist and be writable
- `/templates` must contain `user.html`, `admin.html`
- `app.py` at root

### 6️⃣ Final Test 🚦

- Open Render app URL
- Go to `/` and upload a file as a user
- Go to `/admin` and log in (default: password is `Nuvai$123`)
- Confirm uploads show up in admin view
- Download and delete files to test full flow!

> **Tip:** If you change the admin password, use environment variables instead of hardcoding.

---

## 🪄 Bonus: Improvements

- ✔️ **Sanitize Filenames:**  
  Use `secure_filename()` from Werkzeug when saving files.
- ✔️ **Limit File Size:**  
  In Flask config: `app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024` (10MB)
- ✔️ **File Type Filter:**  
  Check file extension before saving.
- ✔️ **Better Error Feedback:**  
  Show user-friendly messages for all errors.
- ✔️ **Admin Password:**  
  Move to environment variable, never in code.

---

## 💬 Beginner Commentary & Tips

- **Every file has a purpose!**  
  - `app.py` is the brain.  
  - `templates/` are the faces (UI).  
  - `/uploads` is the storage room.  
  - `requirements.txt` is the shopping list.

- **You can test locally with:**  
  ```bash
  python app.py
  ```
  Then visit `http://localhost:5000`

- **Deploying to Render means anyone can use your Docky — just share the URL!**

---

## ❤️ Credits

Made and maintained by [Tharun Kumar](https://github.com/THARUNKUMAR7379)  
Big thanks to Flask, SQLAlchemy, Tailwind CSS, and all open-source devs!

---

**Built with 🧠, ☕, and ❤️ by Tharun**

---

If you have more questions or want a walkthrough on any specific section, just ask!