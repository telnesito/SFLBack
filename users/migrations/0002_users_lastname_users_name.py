# Generated by Django 5.1.2 on 2024-10-23 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='lastname',
            field=models.CharField(default='default', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='name',
            field=models.CharField(default='default', max_length=200),
            preserve_default=False,
        ),
    ]
