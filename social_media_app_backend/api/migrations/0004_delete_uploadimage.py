# Generated by Django 3.1 on 2021-02-18 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_comment_follow_post_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UploadImage',
        ),
    ]
