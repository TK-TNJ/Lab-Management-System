from django.core.management.base import BaseCommand
from student_management_app.models import CustomUser, NotificationStudent, NotificationStaffs, FeedBackStudent, FeedBackStaffs, LeaveReportStudent, LeaveReportStaff, AttendanceReport, Attendance, OnlineClassRoom, StudentResult, Students, Staffs, AdminHOD, Subjects, Courses, SessionYearModel

class Command(BaseCommand):
    help = 'Deletes all users and their associated data from the database'

    def handle(self, *args, **kwargs):
        try:
            # Delete all notifications
            NotificationStudent.objects.all().delete()
            NotificationStaffs.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Successfully deleted all notifications'))

            # Delete all feedback
            FeedBackStudent.objects.all().delete()
            FeedBackStaffs.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Successfully deleted all feedback'))

            # Delete all leave reports
            LeaveReportStudent.objects.all().delete()
            LeaveReportStaff.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Successfully deleted all leave reports'))

            # Delete all attendance records
            AttendanceReport.objects.all().delete()
            Attendance.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Successfully deleted all attendance records'))

            # Delete all online classrooms
            OnlineClassRoom.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Successfully deleted all online classrooms'))

            # Delete all student results
            StudentResult.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Successfully deleted all student results'))

            # Delete all students
            Students.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Successfully deleted all students'))

            # Delete all staff
            Staffs.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Successfully deleted all staff'))

            # Delete all admin/HOD
            AdminHOD.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Successfully deleted all admin/HOD'))

            # Delete all subjects
            Subjects.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Successfully deleted all subjects'))

            # Delete all courses
            Courses.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Successfully deleted all courses'))

            # Delete all session years
            SessionYearModel.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Successfully deleted all session years'))

            # Finally, delete all users
            CustomUser.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Successfully deleted all users'))

            self.stdout.write(self.style.SUCCESS('Successfully deleted all data from the database'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error occurred: {str(e)}')) 