# Generated by Django 3.2.5 on 2021-07-22 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medflow', '0002_timetable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='vacation',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
