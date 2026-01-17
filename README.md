# Business Nexus – Backend (Django REST API)

This repository contains the backend implementation of **Business Nexus**, a platform that connects Entrepreneurs and Investors through meetings, document sharing, and real-time communication.

---

## 🚀 Tech Stack
- Python
- Django
- Django REST Framework
- JWT Authentication
- PostgreSQL / SQLite
- Socket.IO (Video & Real-time features)

---

## 🔐 Authentication
- JWT-based authentication
- Roles supported:
  - Admin
  - Investor
  - Entrepreneur
- Endpoints:
  - Login: `/api/token/`
  - Refresh Token: `/api/token/refresh/`
  - Register: `/api/users/register/`

---

## 👤 User Management
- Admin panel enabled
- Superuser created
- User roles visible in Django Admin
- Pagination enabled in user listing
- Profile API available

---

## 📅 Meetings Module
- Schedule meetings between Investor & Entrepreneur
- Fields:
  - Investor
  - Entrepreneur
  - Start Time
  - End Time
  - Status (Pending, Approved, Completed)
- Endpoints:
  - Schedule Meeting (POST): `/api/meetings/schedule/`
  - Update Meeting: `/api/meetings/<id>/update/`

---

## 📂 Documents Module
- Document upload support
- Backend APIs ready
- Frontend integration completed
- Local testing supported

---

## 🎥 Video Calling (Real-time)
- Socket.IO installed and configured
- Backend ready for real-time communication
- To be tested after deployment

---

## Pending / Not Fully Integrated

- Frontend integration for:
  - Registration/Login
  - Documents page
  - Meetings scheduling
  - Video calling UI
  - Payments UI

> **Note:** Some features are backend-ready but frontend is not fully linked. Demonstration screenshots or mock data may be used for presentation purposes.

## ⚙️ Setup Instructions

```bash
git clone <backend-repo-url>
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
