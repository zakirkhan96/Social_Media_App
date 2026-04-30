# 📱 Social App (Django)

![Django](https://img.shields.io/badge/Django-6.x-green)
![Python](https://img.shields.io/badge/Python-3.14-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Development-orange)

A modern social media web application built with Django.  
Users can create posts, like, comment, and manage profiles with image uploads.

---

## 🚀 Features

- 🔐 Authentication (Login / Logout / Register)
- 📝 Post creation (text + image)
- ❤️ Like system (AJAX, real-time)
- 💬 Comment system (persistent)
- 👤 User profiles with profile pictures
- 📊 Like & comment counters
- ⚡ Dynamic UI (Fetch API)
- 🎨 Tailwind CSS styling

---

## 🛠️ Tech Stack

| Layer      | Tech                     |
|------------|--------------------------|
| Backend    | Django (Python)          |
| Frontend   | HTML, Tailwind, JS       |
| Database   | SQLite (Dev)             |
| Media      | Django Media Files       |

---

## 📂 Project Structure


Social_App/
│
├── accounts/
├── posts/
├── follows/
├── social/
├── templates/
├── static/
├── media/
├── db.sqlite3
└── manage.py


---

## ⚙️ Setup Instructions

### 1. Clone Repo

git clone <your-repo-url>
cd Social_App


### 2. Virtual Environment

python -m venv venv
venv\Scripts\activate


### 3. Install Dependencies

pip install -r requirements.txt


If not available:

pip install django pillow


### 4. Run Migrations

python manage.py makemigrations
python manage.py migrate


### 5. Create Superuser

python manage.py createsuperuser


### 6. Run Server

python manage.py runserver


---


📜 License

MIT License

👨‍💻 Author

Zakir khan
