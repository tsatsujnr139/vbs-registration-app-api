# Generated by Django 2.2.12 on 2020-04-25 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_participant_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='age',
            field=models.IntegerField(),
        ),
    ]