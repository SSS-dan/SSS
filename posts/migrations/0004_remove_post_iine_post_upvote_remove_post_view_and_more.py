# Generated by Django 4.2.1 on 2023-05-23 12:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0003_post_iine_post_view'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='iine',
        ),
        migrations.AddField(
            model_name='post',
            name='upvote',
            field=models.ManyToManyField(related_name='upvoted_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='post',
            name='view',
        ),
        migrations.AddField(
            model_name='post',
            name='view',
            field=models.ManyToManyField(related_name='viewed_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
