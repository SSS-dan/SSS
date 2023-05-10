from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Lecture(models.Model):
    title = models.CharField(max_length=100)
    instructor = models.CharField(max_length=50)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)