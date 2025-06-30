# Django Task Manager

A simple and responsive Task Manager built with Django and Bootstrap. Users can register, log in, and manage their personal task list with deadlines, priorities, and statuses.

---

## Features

-  User registration, login & logout
-  Create, edit, delete your own tasks
-  Set task due dates
-  Mark task priority (Low, Medium, High)
-  Track task status (To Do, In Progress, Done)
-  Secure access – each user only sees their own tasks
-  Clean Bootstrap interface

---

## Test Credentials

You can log in using the following test account:

- **Username**: `macie`  
- **Password**: `test1234!`

---
## How to run

1. **Clone the repository**  
   ```sh
   git clone https://github.com/Utopekk/Task-Manager.git
   ```

2. **Install dependencies**  
   Make sure you have pip installed, then run:
   ```sh
   pip install django
   ```

3. **Run database migrations**  
   ```sh
   python manage.py migrate
   ```

4. **Create a superuser (optional, for admin access)**  
   ```sh
   python manage.py createsuperuser
   ```

5. **Start the development server**  
   ```sh
   python manage.py runserver
   ```
   The app will be available at [http://127.0.0.1:8000/]
