# Generated by Django 5.1.2 on 2024-11-02 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_usersdetails_addres_alter_usersdetails_profile_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usersdetails',
            old_name='addres',
            new_name='address',
        ),
    ]
