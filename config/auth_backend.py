from django.contrib.auth.backends import ModelBackend
from qr_app.models import User
from pybo.models import *
from .crawl_saint import get_saint_cookies, pretty_print_takes_info, get_takes_info, get_student_info

class PasswordlessAuthBackend(ModelBackend):
    """Log in to Django without providing a password.

    """
    def authenticate(self, student_id=None, cookies=None):
        info = get_student_info(cookies)
        try:
            user = User.objects.get(student_id=student_id)
            student = User.get_student_by_id(student_id)
            #print("이미 있음")
        except User.DoesNotExist:
            user = User(student_id=student_id)
            user.save()
            student = User()
        #print(info)
        student.student_id = student_id
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
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None