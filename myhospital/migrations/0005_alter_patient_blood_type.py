# Generated by Django 5.1.2 on 2024-11-03 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myhospital', '0004_alter_diagnosis_disease_alter_diagnosis_remarks_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='blood_type',
            field=models.CharField(choices=[('O', 'O'), ('A', 'A'), ('B', 'B'), ('B+', 'B+'), ('A+', 'A+')], max_length=2),
        ),
    ]
