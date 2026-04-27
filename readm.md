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

## 🔧 Configuration

### settings.py
```python
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
urls.py
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
🧠 Architecture
Like System
AJAX (Fetch API)
Real-time UI update
Stored in database
Comment System
POST + CSRF
Persistent storage
Dynamic rendering
Profile System
OneToOne(User ↔ Profile)
Auto-created via signals
Image storage support
⚠️ Common Issues
Profile not found
python manage.py shell
from django.contrib.auth.models import User
from accounts.models import Profile

for user in User.objects.all():
    Profile.objects.get_or_create(user=user)
Images not showing
Check MEDIA_URL
Check MEDIA_ROOT
Ensure static media serving enabled
Like/Comment not working
Check browser console
Verify JS loading
Check Django views & URLs
🧪 Testing
python manage.py test
📦 requirements.txt
Django>=6.0
Pillow>=10.0
🚀 Deployment Notes
Set DEBUG = False
Use PostgreSQL
Run:
python manage.py collectstatic
Use Gunicorn + Nginx
📜 License

MIT License

👨‍💻 Author

Your Name