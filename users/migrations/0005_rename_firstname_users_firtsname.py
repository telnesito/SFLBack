# Generated by Django 5.1.2 on 2024-10-23 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_rename_firtsname_users_firstname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='firstname',
            new_name='firtsname',
        ),
    ]
