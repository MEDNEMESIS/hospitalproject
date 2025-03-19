# Generated by Django 5.1.2 on 2024-10-29 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myhospital', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosis',
            name='diagnosis_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='date_of_birth',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='treatment_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
