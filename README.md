# Job Application Tracker API

A REST API to track job applications built with Django REST Framework.

## Features
- JWT Authentication (Register/Login)
- Add, Edit, Delete job applications
- Search by company name
- Filter by status (Applied/Interview/Rejected/Hired)

## Tech Stack
- Python
- Django
- Django REST Framework
- JWT Authentication
- SQLite

[//]: # (API Endpoints)
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