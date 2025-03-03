# Contact Management System (Django)

This is a simple Django application to manage contacts. You can add, view, edit, delete, and organize contacts in your system.

## Features

- **Home Page**: Displays a list of all the contacts.
- **Add Contact**: Add new contacts to the system.
- **View All Contacts**: See the complete list of contacts.
- **Edit Contact**: Update existing contact details.
- **Delete Contact**: Delete a contact from the system.
- **Trash**: View all the contacts in the trash (you can delete them permanently).

## What You Need

- **Backend**: Django
- **Frontend**: HTML (using Bootstrap for styling)
- **Database**: SQLite (Django's default database)

## How to Set It Up

### Step 1: Clone the repository

Clone this repository to your computer using this command:

```bash
git clone https://github.com/your-username/contact-management-system.git
```

### Step 2: Set up a virtual environment

Create and activate a virtual environment to manage your dependencies:

```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### Step 3: Install dependencies

Install the required packages:

```bash
pip install -r requirements.txt
```

### Step 4: Create the database tables

Run this command to create the necessary tables for your app:

```bash
python manage.py migrate
```

### Step 5: Create a superuser (optional)

You can create an admin user to access the Django admin panel:

```bash
python manage.py createsuperuser
```

### Step 6: Run the server

Start the server with this command:

```bash
python manage.py runserver
```

You can now open your browser and go to `http://127.0.0.1:8000/` to use the app.

## How to Use

- **Home Page**: Displays a list of all the contacts.
- **Add Contact**: Add new contacts by filling in their first name, last name, phone number, and email.
- **View All Contacts**: View all the contacts you have added.
- **Edit Contact**: Edit any existing contact's details.
- **Delete Contact**: Delete a contact from the system.
- **Trash**: View all the contacts in the trash.

## Project Structure

```
contact_management_system/
│
├── contacts/                    # App for managing contacts
│   ├── models.py                # Defines how contacts are stored
│   ├── views.py                 # Handles how data is displayed
│   ├── forms.py                 # Handles forms for adding/editing contacts
│   ├── templates/               # Folder with HTML files for each page
│   └── migrations/              # Database migrations
│
├── contact_management_system/   # Main project folder
│   ├── settings.py              # Django settings
│   ├── urls.py                  # URL mappings for the app
│   ├── wsgi.py                  # Web server configuration
│   └── asgi.py                  # Asynchronous server configuration
│
├── manage.py                    # Command-line script to manage the project
├── requirements.txt             # List of Python packages needed for the project
└── README.md                    # This file
```
