# Generated by Django 4.2.1 on 2023-05-26 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_post_upvote_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='view_num',
            field=models.IntegerField(default=0),
        ),
    ]