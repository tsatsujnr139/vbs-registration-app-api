# Generated by Django 2.2.24 on 2021-06-06 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]