# Generated by Django 5.1.2 on 2024-10-29 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myhospital', '0003_alter_patient_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosis',
            name='disease',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='diagnosis',
            name='remarks',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='diagnosis',
            name='temperature',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='address',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='contact',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='designation',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='specialization',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='patient',
            name='blood_type',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='patient',
            name='kin_contact',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='patient',
            name='next_of_kin',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_method',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='payment',
            name='received_by',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='prescription',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='recommendations',
            field=models.CharField(max_length=50),
        ),
    ]
