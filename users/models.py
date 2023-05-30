from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.validators import RegexValidator


class User(AbstractBaseUser, PermissionsMixin):
    student_id = models.CharField(max_length=15, primary_key=True, unique=True, default='')
    name = models.CharField(max_length=30, default='')
    state = models.IntegerField(default=0)
    year = models.IntegerField(null=True)
    semester = models.IntegerField(null=True)
    major = models.CharField(max_length=100, null=True)
    advisor = models.CharField(max_length=30, null=True)
    login_cookie = models.CharField(max_length=50, null=True)
    nickname = models.CharField(max_length=30, default='', null=True)
    objects = models.Manager()

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    USERNAME_FIELD = 'student_id'
    REQUIRED_FIELDS = []

    @classmethod
    def get_student_by_id(cls, student_id):
        return cls.objects.get(student_id=student_id)

    @classmethod
    def get_login_cookie(cls, student_id):
        return cls.objects.get(student_id=student_id).login_cookie

    def update_student_major(self, new_major):
        self.major = new_major
        self.save()

    def update_student_name(self, new_name):
        self.name = new_name
        self.save()

    def update_student_state(self, new_state):
        self.state = new_state
        self.save()

    def update_student_grade(self, new_year, new_semester):
        self.year = new_year
        self.semester = new_semester
        self.save()

    def update_student_cookie(self, new_cookie):
        self.cookie = new_cookie
        self.save()

    def delete_student(self):
        self.delete()

    @classmethod
    def get_takes(cls, student_id):
        return cls.objects.get(student_id=student_id).takes


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/')
