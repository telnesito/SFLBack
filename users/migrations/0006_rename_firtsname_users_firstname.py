# Generated by Django 5.1.2 on 2024-10-23 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_rename_firstname_users_firtsname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='firtsname',
            new_name='firstname',
        ),
    ]
