# Generated by Django 5.1.2 on 2024-10-26 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_rename_firtsname_users_firstname'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Users',
        ),
    ]
