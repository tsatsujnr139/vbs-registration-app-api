# Generated by Django 3.2.13 on 2022-06-01 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20220515_1924'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='attendance_type',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='session',
        ),
    ]
