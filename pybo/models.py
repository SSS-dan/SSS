from django.db import models
import datetime
from users.models import User

# Create your models here.


class Course(models.Model):
    course_id = models.CharField(max_length=10, null=True)
    semester = models.IntegerField()
    name = models.CharField(max_length=30, null=True)
    day = models.IntegerField()
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    classroom = models.CharField(max_length=15, default='')
    advisor = models.CharField(max_length=30)
    major = models.CharField(max_length=30, null=True)
    objects = models.Manager()

    @classmethod
    def get_course_by_id(cls, course_id, semester):
        try:
            return cls.objects.get(course_id=course_id, semester=semester)
        except cls.DoesNotExist:
            return None

    def update_name(self, new_name):
        self.name = new_name
        self.save()

    def update_time(self, new_day, start_hour, start_minute, end_hour, end_minute):
        self.day = new_day
        self.start_time = datetime.time(start_hour, start_minute)
        self.end_time = datetime.time(end_hour, end_minute)
        self.save()

    def update_classroom(self, new_classroom):
        self.classroom = new_classroom
        self.save()

    def delete_course(self):
        self.delete()


class Takes(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='takes')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    middle_grade = models.FloatField(null=True)
    final_grade = models.FloatField(null=True)
    real = models.BooleanField()
    objects = models.Manager()

    def delete_takes(self):
        self.delete()


class Notice(models.Model):
    mod = models.IntegerField()
    num = models.IntegerField()
    title = models.CharField(max_length=100, null=True)
    url = models.URLField(null=True)
    writer = models.CharField(max_length=100, null=True)
    file = models.URLField(null=True)   # 링크 넣는곳
    date = models.DateField()
    view = models.IntegerField()
    objects = models.Manager()


__all__ = ['Course', 'Takes', "Notice"]
