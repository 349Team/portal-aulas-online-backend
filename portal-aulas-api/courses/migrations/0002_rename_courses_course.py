# Generated by Django 4.0.10 on 2023-04-09 02:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Courses',
            new_name='Course',
        ),
    ]