# Generated by Django 5.1.2 on 2024-10-27 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_usersdetails_user_role_alter_usersdetails_ci_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersdetails',
            name='profile_image',
            field=models.ImageField(default='null', upload_to='miniatura/'),
            preserve_default=False,
        ),
    ]
