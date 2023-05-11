from django.contrib.auth.backends import ModelBackend
from qr_app.models import NewUser
from pybo.models import *
from .crawl_saint import get_saint_cookies, pretty_print_takes_info, get_takes_info, get_student_info

User_model = NewUser

class PasswordlessAuthBackend(ModelBackend):
    """Log in to Django without providing a password.

    """
    def authenticate(self, username=None, cookies=None):
        info = get_student_info(cookies)
        try:
            user = User_model.objects.get(username=username)
            student = Student.get_student_by_id(username)
            #print("이미 있음")
        except User_model.DoesNotExist:
            user = User_model(username=username)
            user.save()
            student = Student()
        #print(info)
        student.student_id = username
        student.name = info['성명']
        student.state = 1
        student.year = int(info['현학년/학기'][0])
        student.semester = int(info['현학년/학기'].split("/")[-1].strip().replace("학기",""))
        student.advisor = info['지도교수']
        student.login_cookie = cookies
        student.save()
        return user


    def get_user(self, user_id):
        try:
            return User_model.objects.get(pk=user_id)
        except User_model.DoesNotExist:
            return None