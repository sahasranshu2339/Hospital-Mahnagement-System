# Hospital Management System

A Django-based hospital management system for handling patient registration, login, role-based dashboards, and hospital operations using a lightweight SQLite database.

## Overview

This project is built with Python and Django and includes:

- Patient registration and login
- User role management for patients, doctors, and administrators
- Patient dashboard
- Doctor dashboard
- Admin dashboard
- SQLite database integration
- HTML templates for the user interface

## Tech Stack

- Python
- Django
- SQLite
- HTML / CSS / Bootstrap-style templates

## Project Structure

```text
Hospital-Mahnagement-System/
├── Hspital_management_system/
│   ├── Hospital_app/
│   ├── Hspital_management_system/
│   ├── templates/
│   ├── manage.py
│   ├── db.sqlite3
│   ├── package-lock.json
│   └── .gitignore
├── README.md
└── .git/
```

## Features

- Registration flow for users
- Authentication and authorization using Django's built-in auth system
- Role-based redirects after login
- Dashboards for different user roles
- Database models for `UserProfile`, `Doctor`, and `Patient`

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/sahasranshu2339/Hospital-Mahnagement-System.git
cd Hospital-Mahnagement-System
```

2. Create and activate a virtual environment:

```bash
cd Hspital_management_system
python -m venv venv
```

On macOS/Linux:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

3. Install Django:

```bash
pip install django
```

4. Apply database migrations:

```bash
python manage.py migrate
```

5. Start the development server:

```bash
python manage.py runserver
```

6. Open the application in your browser:

```text
http://127.0.0.1:8000/
```

## Admin Access

You can create a superuser to access the Django admin panel:

```bash
python manage.py createsuperuser
```

Then log in at:

```text
http://127.0.0.1:8000/admin/
```

## Notes

- The project currently uses Django's default SQLite database configuration.
- The repository contains a nested project directory named `Hspital_management_system`.
- If you want to deploy this project for production, configure `ALLOWED_HOSTS`, environment variables, and secure settings before using it in a live environment.

## License

This project does not currently include a license file. If needed, add one before publishing or distributing the project.
