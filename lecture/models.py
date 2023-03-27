from django.db import models

class Lecture(models.Model):
    title = models.CharField(max_length=100)
    instructor = models.CharField(max_length=50)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()