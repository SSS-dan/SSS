from django.db import models
from users.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='', related_name='posts')
    mod = models.IntegerField()

    upvote = models.ManyToManyField(User, related_name='upvoted_posts')
    upvote_num = models.IntegerField(default=0)

    view = models.ManyToManyField(User, related_name='viewed_posts')
    view_num = models.IntegerField(default=0)

    def delete_post(self):
        self.delete()


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='', related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def delete_comment(self):
        self.delete()
