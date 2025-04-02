# Student Management System

A comprehensive Django-based Student Management System that allows educational institutions to manage students, staff, and administrative tasks efficiently.

## Features

- Multi-role user system (Admin/HOD, Staff, Students)
- Real-time notifications using Firebase
- Attendance management
- Course and subject management
- Leave management
- Feedback system
- Result management
- Online classroom functionality

## Technology Stack

- Python 3.x
- Django
- MySQL Database
- Bootstrap 4
- AdminLTE Template
- Firebase Cloud Messaging

## Prerequisites

- Python 3.x
- MySQL Server
- Virtual Environment (recommended)

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd student-management-system
```

2. Create and activate virtual environment:
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure MySQL database:
- Create a database named 'lab_management_system'
- Update database settings in settings.py

5. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

## Project Structure

```
student_management_system/
├── student_management_app/
│   ├── templates/
│   │   ├── hod_template/
│   │   ├── staff_template/
│   │   └── student_template/
│   ├── models.py
│   ├── views.py
│   └── ...
├── student_management_system/
│   ├── settings.py
│   ├── urls.py
│   └── ...
└── manage.py
```

## User Roles

1. **Admin/HOD**
   - Manage staff and students
   - Create courses and subjects
   - View attendance reports
   - Manage leave requests
   - Send notifications

2. **Staff**
   - Take attendance
   - Manage results
   - Apply for leave
   - Send notifications to students
   - Create online classrooms

3. **Student**
   - View attendance
   - View results
   - Apply for leave
   - Submit feedback
   - Join online classrooms

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

[![Open Source Love](https://badges.frapsoft.com/os/mit/mit.svg?v=102)](https://github.com/hackstarsj/student_management_system_part_11/raw/master/LICENSE)

<pre>
admin@gmail.com
admin
</pre>


<br>
<br>

<h2>Installation Steps : </h2>

<p>Project Dependency :</p>
<pre>
pip install requests
pip install Django
pip install mysql-client
pip install mysqlclient
</pre>
<hr>
<ul>
<ol>Change Database Setting in settings.py </ol>
<ol>
Run Migration Command 
<pre>
python manage.py makemigrations
python manage.py migrate
</pre>
</ol>
<ol>
Run Project python runserver
</ol>
</ul>

