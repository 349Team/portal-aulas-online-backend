# Generated by Django 4.0.10 on 2023-06-19 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0018_remove_anotation_anotations_anotation_link_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anotation',
            name='title',
        ),
    ]
