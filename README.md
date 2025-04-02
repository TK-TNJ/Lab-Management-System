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
<ol>First Create MySql Database Tutorial : <a href="https://youtu.be/cEazlDKu86E">https://youtu.be/cEazlDKu86E</a> </ol>
<ol>Change Database Setting in settings.py </ol>
<ol>
Run Migration Command 
<pre>
python manage.py makemigrations
python manage.py migrate
</pre>
 <ul>     
<li>In login_page.html Replace <pre>CAPTCHA_CLIENT_KEY</pre> with Captcha Client Side Key</li>
<li>In views.py Replace <pre>CAPTCHA_SERVER_KEY</pre> with Captcha SERVER Side Key</li>
<li>For Captcha Key Visit <a href="https://www.google.com/recaptcha/intro/v3.html">https://www.google.com/recaptcha/intro/v3.html</a></li>
</ul>
</ol>
<ol>
Run Project python runserver
</ol>
</ul>
<hr>
<b>For Video Confrencing Using This Library Complete Demo Project : <a href="https://www.rtcmulticonnection.org/">https://www.rtcmulticonnection.org/</a></b>
<hr>
<h2>Complete Video Course</h2>
<div align="center" style="width:100%">
      <a href="https://www.youtube.com/playlist?list=PLb-NlfexLTk_tUlAPj05s2zc8JgHTVkpH">
     <img 
      src="https://img.youtube.com/vi/y3llbdTtam4/maxresdefault.jpg" 
      alt="Student management System" 
      style="width:100%;">
      </a>
</div>

<h2>Database Design</h2>

<img src="https://github.com/hackstarsj/student_management_system_part_11/blob/master/screenshots/database.png" alt="Database Design">

<h2>Video Confrencing Class Room</h2>
<img src="https://github.com/hackstarsj/student_management_system_part_11/blob/master/screenshots/video_class.jpg" alt="Add Course">


<h2>Add Course Page</h2>
<img src="https://github.com/hackstarsj/student_management_system_in_django/blob/master/screenshots/add_course.PNG" alt="Add Course">
                                                                                                                                   
<h2>Add Student Page</h2>
<img src="https://github.com/hackstarsj/student_management_system_in_django/blob/master/screenshots/add_student_dj.PNG" alt="Add Student">
                                                                                                                                        

<h2>Add Staff Page</h2>
<img src="https://github.com/hackstarsj/student_management_system_in_django/blob/master/screenshots/add_staff.PNG" alt="Add Staff">

<h2>Add Subject Page</h2>
<img src="https://github.com/hackstarsj/student_management_system_in_django/blob/master/screenshots/add_subject.PNG" alt="Add Subject">


<h2>Manage Subject Page</h2>
<img src="https://github.com/hackstarsj/student_management_system_in_django/blob/master/screenshots/manage_subject.PNG" alt="Add Subject">


<h2>Manage Course Page</h2>
<img src="https://github.com/hackstarsj/student_management_system_in_django/blob/master/screenshots/manage_course.PNG" alt="Add Subject">


<h2>Manage Staff Page</h2>
<img src="https://github.com/hackstarsj/student_management_system_in_django/blob/master/screenshots/manage_staff.PNG" alt="Add Subject">


<h2>Manage Student Page</h2>
<img src="https://github.com/hackstarsj/student_management_system_in_django/blob/master/screenshots/manage_subject.PNG" alt="Add Subject">

<h2>Staff Take Attendance Page</h2>
<img src="https://raw.githubusercontent.com/hackstarsj/student_management_system_part_11/master/screenshots/take_attendance.PNG"  alt="Take Attendance Page">

<h2>Staff View and Update Attendance Page</h2>
<img src="https://github.com/hackstarsj/student_management_system_part_11/blob/master/screenshots/view_attendance.PNG?raw=true"  alt="Staff View and Update Attendance Page">


<h2>Session Year Manage</h2>
<img src="https://raw.githubusercontent.com/hackstarsj/student_management_system_part_11/master/screenshots/session_year.PNG"  alt="Session Year Manage">

<h2>Staff Apply for Leave</h2>
<img src="https://raw.githubusercontent.com/hackstarsj/student_management_system_part_11/master/screenshots/leave_message.PNG"  alt="Staff Apply for Leave">

<h2>Staff Feedback Message</h2>
<img src="https://raw.githubusercontent.com/hackstarsj/student_management_system_part_11/master/screenshots/feedback_message.PNG"  alt="Staff Feedback Message">


<h2>Password Reset Form</h2>
<img src="https://raw.githubusercontent.com/hackstarsj/student_management_system_part_11/master/screenshots/password_reset_1.PNG"  alt="Password Reset">

<h2>Password Change Form</h2>
<img src="https://raw.githubusercontent.com/hackstarsj/student_management_system_part_11/master/screenshots/password_reset_2.PNG"  alt="Password Reset">


<h2>Student View Attendance Form</h2>
<img src="https://raw.githubusercontent.com/hackstarsj/student_management_system_part_11/master/screenshots/student_view_attenndance.PNG"  alt="Student View Attendance Form">

<h2>Student View Attendance Data</h2>
<img src="https://raw.githubusercontent.com/hackstarsj/student_management_system_part_11/master/screenshots/attendance_data.PNG"  alt="Student View Attendance Data">

<h2>Student Apply for Leave</h2>
<img src="https://raw.githubusercontent.com/hackstarsj/student_management_system_part_11/master/screenshots/student_leave.PNG"  alt="Student Apply for Leave">

<h2>Student Send Feedback Message</h2>
<img src="https://raw.githubusercontent.com/hackstarsj/student_management_system_part_11/master/screenshots/student_feedback.PNG"  alt="Student Send Feedback Message">

<h2>HOD Reply Student Feedback</h2>
<img src="https://raw.githubusercontent.com/hackstarsj/student_management_system_part_11/master/screenshots/feedback_student.PNG"  alt="HOD Reply Student Feedback">

<h2>HOD Reply Staff Feedback</h2>
<img src="https://raw.githubusercontent.com/hackstarsj/student_management_system_part_11/master/screenshots/feedback_staff.PNG"  alt="HOD Reply Staff Feedback">

<h2>HOD Approve and Disapprove Student Leave</h2>
<img src="https://raw.githubusercontent.com/hackstarsj/student_management_system_part_11/master/screenshots/student_leave_approve.PNG"  alt="HOD Approve and Disapprove Student Leave">

<h2>HOD Approve and Disapprove Staff Leave</h2>
<img src="https://raw.githubusercontent.com/hackstarsj/student_management_system_part_11/master/screenshots/staff_leave_approve.PNG"  alt="HOD Approve and Disapprove Staff Leave">

<h2>HOD View Attendance Data</h2>
<img src="https://raw.githubusercontent.com/hackstarsj/student_management_system_part_11/master/screenshots/admin_view_attendance.PNG"  alt="HOD View Attendance Data">

<h2>HOD Profile View and Update</h2>
<img src="https://raw.githubusercontent.com/hackstarsj/student_management_system_part_11/master/screenshots/admin_profile.PNG"  alt="HOD Profile View and Update">


<h2>Staff Profile View and Update</h2>
<img src="https://raw.githubusercontent.com/hackstarsj/student_management_system_part_11/master/screenshots/staff_profile.PNG"  alt="Staff Profile View and Update">


<h2>Student Profile View and Update</h2>
<img src="https://raw.githubusercontent.com/hackstarsj/student_management_system_part_11/master/screenshots/student_profile.PNG"  alt="Student Profile View and Update">

<h2>Student Homepage</h2>
<img src="https://raw.githubusercontent.com/hackstarsj/student_management_system_part_11/master/screenshots/student_homepage.PNG"  alt="Student Homepage">

<h2>Staff Homepage</h2>
<img src="https://raw.githubusercontent.com/hackstarsj/student_management_system_part_11/master/screenshots/staff_homepage.PNG"  alt="Staff Homepage">

<h2>Admin Homepage</h2>
<img src="https://raw.githubusercontent.com/hackstarsj/student_management_system_part_11/master/screenshots/admin_homepage.PNG"  alt="Admin Homepage">
<br>
<img src="https://raw.githubusercontent.com/hackstarsj/student_management_system_part_11/master/screenshots/admin_homepage2.PNG"  alt="Admin Homepage">
<hr>
<hr>
<h1>Extending Project Parts</h1>
<h2>Add Student Results From Staff Panel</h2>
<img src="https://raw.githubusercontent.com/hackstarsj/student_management_system_part_11/master/screenshots/add_result2.PNG"  alt="Add Results">
