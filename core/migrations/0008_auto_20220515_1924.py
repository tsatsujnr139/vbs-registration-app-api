# Generated by Django 3.2.13 on 2022-05-15 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20210612_0114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='contact_no',
            field=models.CharField(max_length=13),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='whatsApp_no',
            field=models.CharField(blank=True, max_length=13),
        ),
    ]
