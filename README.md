# login-system-django

# Custom User Authentication System

A Django-based system for user registration and login featuring a custom user and superuser model.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)

## Features

- Custom user and superuser models.
- User registration and login.
- Authentication via Django's built-in system.
- No password recovery (can be added later).
  
## Technologies Used

- **Django**: Web framework for building the authentication system.
- **SQLite** (default): Lightweight database used for development.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name

2. Create and activate a virtual environment

```python
    python -m venv .venv # On Windows
    python3 -m venv .venv # On Linux
    
    .venv\Scripts\activate # On Windows
    source .venv/bin/activate
```

3. Install the required dependencies.

```python
    pip install -r requirement.txt
```
4. Run the initial database migrations.

```python
    python manage.py migrate # On Windows
    python3 manage.py migrate # On Linux
```

5. Run the development server.

```python
    python manage.py runserver # On Windows
    python3 manage.py runserver # On Linux
```

6. Open your browser and go to http://1270.0.1:8000/

## Usage

### User Registration
Users can sign up navigating to ```/``` and filling out the registration form

### User Login
Registered users can log in through the ```/login/``` page, and auto redirect to ```/welcome/``` page.

