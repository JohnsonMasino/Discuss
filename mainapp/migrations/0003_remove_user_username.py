# Generated by Django 5.0 on 2023-12-10 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]