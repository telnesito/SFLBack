# Generated by Django 5.1.2 on 2024-11-02 03:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treatments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HealingTreatment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_treatment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='treatments.treatment')),
                ('video', models.FileField(upload_to='healings/')),
                ('image', models.FileField(upload_to='healings/')),
            ],
        ),
        migrations.CreateModel(
            name='MedicineTreatment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_treatment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='treatments.treatment')),
                ('dosis', models.CharField(max_length=50)),
                ('presentation', models.CharField(max_length=100)),
                ('unit', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DailyTreatment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('taken', models.BooleanField(default=False)),
                ('notes', models.TextField(blank=True, null=True)),
                ('id_treatment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='daily_treatments', to='treatments.treatment')),
            ],
        ),
    ]
