# Library Management System

A comprehensive Django web application for managing library books, users, and borrowings.

## Features

- User authentication (registration, login, logout, profile)
- Full CRUD operations for books
- Book borrowing and return system with fine calculation
- Advanced search and filtering
- Bootstrap 5 responsive UI
- Admin panel for management

## Technologies Used

- Django 6.0.6
- SQLite (default database)
- Bootstrap 5
- django-crispy-forms
- django-filter
- crispy-bootstrap5

## Installation

### 1. Clone the repository
```bash
git clone [your-repository-url]
cd library_system
2. Create and activate virtual environment
bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
3. Install dependencies
bash
pip install -r requirements.txt
4. Apply migrations
bash
python manage.py makemigrations
python manage.py migrate
5. Create superuser (admin)
bash
python manage.py createsuperuser
6. Load sample books (optional)
bash
python manage.py shell
# Then run the Python script to add books
7. Run the server
bash
python manage.py runserver
8. Open in browser
text
http://127.0.0.1:8000/
Default Admin Credentials
text
Username: socmrbrut
Email: aoterenbruh@gmail.com
Password: [your-password]
Project Structure
text
library_system/
├── books/          # Book management app
│   ├── models.py   # Book model with CRUD operations
│   ├── views.py    # List, Detail, Create, Update, Delete views
│   ├── forms.py    # Book form with validation
│   └── filters.py  # Search and filter functionality
├── users/          # User authentication and profiles
│   ├── models.py   # UserProfile model
│   ├── forms.py    # Registration and login forms
│   └── signals.py  # Auto-create profile on user registration
├── borrowings/     # Borrowing records and fines
│   ├── models.py   # BorrowRecord model with fine calculation
│   └── views.py    # Borrow and return functionality
├── templates/      # HTML templates with Bootstrap 5
├── static/         # CSS and static files
└── library_project/ # Project settings
Main Features
Books Management
✅ Add, view, edit, delete books

✅ Search by title, author, genre

✅ Filter by year range

✅ Track available copies

User Authentication
✅ Registration with email and phone

✅ Login/Logout

✅ User profile with user type (student, teacher, admin, librarian)

Borrowing System
✅ Borrow books (with availability check)

✅ Return books with fine calculation ($0.50 per day overdue)

✅ View all borrowings (admin) and my borrowings (user)

Admin Panel
✅ Full CRUD operations

✅ Manage users, books, and borrowings

✅ Search and filter in admin

Testing
bash
python manage.py test
Demo Credentials
text
Admin: socmrbrut / [your-password]
Regular User: Create your own account
Database
The project uses SQLite database by default. The database file is:

text
db.sqlite3
Troubleshooting
Common Issues
ModuleNotFoundError: No module named 'django'

bash
pip install -r requirements.txt
TemplateDoesNotExist: bootstrap4/uni_form.html

bash
pip install crispy-bootstrap5
Database errors

bash
python manage.py migrate
Team Members and Contributions
Member	Role	Contribution
Team Leader	Full Stack Developer	Project setup, models, views, templates
Member 2	Backend Developer	Authentication, borrowing system
Member 3	Frontend Developer	Templates, CSS, Bootstrap
Member 4	Tester	Testing and documentation
License
This project is created for educational purposes.

Contact
For any questions, please contact the team leader.

Demo Video
[Link to demo video]

GitHub Repository
[Link to GitHub repository]

text

## Создание requirements.txt сейчас:

```powershell
# Создать новый requirements.txt с правильными версиями
pip freeze > requirements.txt

# Или вручную создать файл с таким содержимым:
Создайте файл requirements.txt с этим содержимым:

txt
Django==6.0.6
django-crispy-forms==2.6
crispy-bootstrap5==2026.3
django-filter==25.1
Pillow==12.2.0
asgiref==3.11.1
sqlparse==0.5.5
tzdata==2026.2