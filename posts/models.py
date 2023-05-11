from django.db import models
from pybo.models import Student

# Create your models here.


class Post(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='post')
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def delete_post(self):
        self.delete()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def delete_comment(self):
        self.delete()
