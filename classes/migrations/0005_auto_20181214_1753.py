# Generated by Django 2.0.6 on 2018-12-14 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0004_student_gender'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['name']},
        ),
    ]
