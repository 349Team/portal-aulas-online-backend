# Generated by Django 4.0.10 on 2023-04-09 05:14

import courses.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_rename_courses_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='banner',
            field=models.FileField(upload_to=courses.models.get_file_path),
        ),
    ]
