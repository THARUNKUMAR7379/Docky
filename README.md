```markdown
# 🚢 Docky

**Docky** — Your mini Google Form, now with admin superpowers.  
Submit docs, see docs, and pretend you’re the boss. No logins, no drama! 😄

---

## 🚀 Features

- 👤 **User Dashboard:**  
  A clean form to submit your name and upload any document. Say goodbye to confusing forms!

- 🛡️ **Admin Dashboard:**  
  View all submissions in a slick table: name, clickable/downloadable document, and ⏱️ timestamp.

- 📦 **Local File Storage:**  
  Files saved safely in the `uploads/` folder.

- 🗄️ **SQLite Database:**  
  No MySQL headaches — just pure, simple SQLite.

- 🧾 **Simple HTML Templates:**  
  `user.html` and `admin.html` — classic, clean, and easy to tweak.

- 🚫 **No Login Needed:**  
  Anyone can submit, anyone can view (if they know the admin URL).

- 💯 **Open Source:**  
  Perfect for student projects, intern submissions, or anyone learning Flask!

---

## 🧰 Tech Stack

- **Backend:** Python 3.x & Flask
- **Database:** SQLite (built-in, zero config)
- **Frontend:** HTML5 templates
- **File Storage:** Local `uploads/` folder

---

## 🗂 Project Structure

```
Docky/
├── app.py
├── uploads/
│   └── [your_uploaded_files_here]
├── templates/
│   ├── user.html
│   └── admin.html
├── requirements.txt
└── README.md
```

*If you ever get lost, just remember: uploads go in `uploads/`, templates go in `templates/`, and all roads lead to `app.py`!*

---

## ⚙️ Installation Guide

Get Docky up and running in 2 minutes flat! ⏳

1. **Clone the repo:**
   ```bash
   git clone https://github.com/THARUNKUMAR7379/Docky.git
   cd Docky
   ```

2. **Set up a virtual environment (recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🧪 How to Run Locally

Start your Docky server with a single command:

```bash
python app.py
```

- **User Dashboard:** [http://localhost:5000/](http://localhost:5000/)
- **Admin Dashboard:** [http://localhost:5000/admin](http://localhost:5000/admin)

*If it works on your machine, it’s basically production-ready, right? 😉*

---

## ☁️ Deployment on Render

Want to go live? Here’s how to deploy Docky on [Render](https://render.com):

1. **Create a new Web Service** on Render.
2. **Connect your GitHub repo** (or upload manually).
3. **Build Command:**  
   ```bash
   pip install -r requirements.txt
   ```
4. **Start Command:**  
   ```bash
   python app.py
   ```
5. **Persistent Storage:**  
   For file uploads, add a [Render Disk](https://render.com/docs/disks) and mount it to the `uploads/` folder.

6. **Hit Deploy!**  
   Your app should now be live. Share your Render URL and let the submissions roll in!

---

## 📁 File Upload Details

- **Supported Formats:**  
  - PDF, DOCX, TXT, PPT, XLSX, JPG, PNG, and more — basically, if your browser lets you pick it, Docky stores it!
- **Storage:**  
  All uploaded files are saved in the local `uploads/` folder (so don’t delete it).

---

## 💡 Future Improvements

Wondering what’s next for Docky? Here are some cool ideas:

- 🔒 Add user authentication
- 🕵️‍♂️ File type & size validation
- 📬 Email notifications for new submissions
- 📊 Dashboard charts & analytics
- ☁️ Integration with cloud storage (S3, GDrive)
- 🖌️ Add some stylish CSS (Docky deserves a glow-up!)

*Got a wild idea? Fork it, build it, and share it back!*

---

## 👨‍💻 Author & Contact

**Made by:** [Tharun Kumar](https://github.com/THARUNKUMAR7379)  
**GitHub:** [THARUNKUMAR7379/Docky](https://github.com/THARUNKUMAR7379/Docky)  
**Contact:** Open an issue, or reach out via GitHub!

---

## 🎁 Bonus: Why Use Docky?

- 100% open-source and beginner-friendly
- Great for student/intern projects
- No setup nightmares
- The fastest way to collect documents without the fuss

---

**Built with ❤️ by Tharun**

```
