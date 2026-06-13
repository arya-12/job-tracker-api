# Job Application Tracker

A Full Stack Job Application Tracker built with Django REST Framework backend and HTML/CSS/JS/Tailwind frontend.

## Features
- JWT Authentication (Register/Login/Logout)
- Auto Refresh Token — user logged in rehta hai
- Add, Edit, Delete job applications
- Search by company name
- Filter by status (Applied/Interview/Rejected/Hired)
- Clean responsive UI with Tailwind CSS

## Tech Stack
- Python
- Django
- Django REST Framework
- JWT Authentication
- SQLite
- HTML/CSS/JavaScript
- Tailwind CSS

## Pages
| Page | URL | Description |
|------|-----|-------------|
| Login | / | User login |
| Register | /register/ | Naya user register |
| Dashboard | /dashboard/ | Saari applications dekho |
| Add Job | /add-job/ | Naya job add karo |

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/register/ | Register new user |
| POST | /api/login/ | Login |
| POST | /api/token/refresh/ | Refresh Token |
| GET | /api/jobs/ | Get all jobs |
| POST | /api/jobs/ | Add new job |
| GET | /api/jobs/1/ | Get single job |
| PUT | /api/jobs/1/ | Update job |
| DELETE | /api/jobs/1/ | Delete job |

## Search & Filter
- Search by company name: `/api/jobs/?search=google`
- Filter by status: `/api/jobs/?status=Applied`

## Setup
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to open the app.