# Generated by Django 3.2 on 2021-05-03 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_remove_students_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='contact',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='students',
            name='dob',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='students',
            name='prn',
            field=models.CharField(max_length=15),
        ),
    ]
