# Todoist - Django Task Management App

A simple and elegant task management application built with Django. This application allows users to create, read, update, and delete tasks with a clean and intuitive interface.

## Features

- ✅ Create new tasks
- ✅ Mark tasks as complete/incomplete
- ✅ Update existing tasks
- ✅ Delete tasks
- ✅ View all tasks in a clean interface
- ✅ Responsive design

## Tech Stack

- **Backend**: Django 4.2.23
- **Database**: PostgreSQL (with SQLite fallback for development)
- **Frontend**: HTML, CSS (Bootstrap-ready)
- **Python**: 3.9+

## Installation

### Prerequisites

- Python 3.9 or higher
- pip (Python package installer)
- PostgreSQL 12+ (recommended) or SQLite for development

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd todoist
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env file with your database credentials
   ```

5. **Set up PostgreSQL database**
   ```bash
   # Create a PostgreSQL database
   createdb TasksDB
   # Or using psql:
   # psql -U postgres -c "CREATE DATABASE TasksDB;"
   ```

6. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

8. **Start the development server**
   ```bash
   python manage.py runserver
   ```

9. **Access the application**
   Open your browser and navigate to `http://127.0.0.1:8000/`

## Project Structure

```
todoist/
├── manage.py
├── todoist/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── myapp/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   └── templates/
│       └── tasks/
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
└── LICENSE
```

## Models

### Tasks Model

- `title`: CharField - The task title (max 300 characters)
- `complete`: BooleanField - Task completion status (default: False)
- `created`: DateTimeField - Task creation timestamp

## Environment Variables

The application uses environment variables for configuration. Copy `.env.example` to `.env` and update the values:

## Usage

1. **Adding a Task**: Click on "Add Task" or use the form to create a new task
2. **Viewing Tasks**: All tasks are displayed on the main page
3. **Updating a Task**: Click on the edit button next to any task
4. **Deleting a Task**: Click on the delete button and confirm
5. **Marking Complete**: Toggle the completion status of tasks

## API Endpoints

The application provides the following URL patterns:

- `/` - Main task list view
- `/insert/` - Add new task
- `/update/<id>/` - Update existing task
- `/delete/<id>/` - Delete task

## Development

### Running Tests

```bash
python manage.py test
```

### Collecting Static Files

```bash
python manage.py collectstatic
```

### Making Migrations

```bash
python manage.py makemigrations myapp
python manage.py migrate
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## Deployment

For production deployment, remember to:

1. Set `DEBUG = False` in settings.py
2. Configure `ALLOWED_HOSTS`
3. Use environment variables for sensitive data
4. Use a production database (PostgreSQL recommended)
5. Configure static file serving
6. Set up proper security headers

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you encounter any issues or have questions, please feel free to open an issue on the repository.

## Acknowledgments

- Built with Django framework
- Inspired by modern task management applications
- Thanks to the Django community for excellent documentation
