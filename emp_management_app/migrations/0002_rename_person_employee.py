# Generated by Django 4.2.1 on 2023-06-01 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emp_management_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Person',
            new_name='Employee',
        ),
    ]