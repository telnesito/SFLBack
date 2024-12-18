# Generated by Django 5.1.2 on 2024-10-27 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_remove_usersdetails_id_alter_usersdetails_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersdetails',
            name='user_role',
            field=models.CharField(choices=[('NURSE', 'Nurse'), ('PATIENT', 'Patient')], default='nurse', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usersdetails',
            name='ci',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='usersdetails',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
    ]
