# Generated by Django 3.2.15 on 2022-08-28 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_participantattendance_participantpickup'),
    ]

    operations = [
        migrations.AddField(
            model_name='participantpickup',
            name='day_1_pickup_person',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='participantpickup',
            name='day_2_pickup_person',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='participantpickup',
            name='day_3_pickup_person',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='participantpickup',
            name='day_4_pickup_person',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='participantpickup',
            name='day_5_pickup_person',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.CreateModel(
            name='PickupCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_1', models.CharField(db_index=True, max_length=5)),
                ('day_2', models.CharField(db_index=True, max_length=5)),
                ('day_3', models.CharField(db_index=True, max_length=5)),
                ('day_4', models.CharField(db_index=True, max_length=5)),
                ('day_5', models.CharField(db_index=True, max_length=5)),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.participant')),
            ],
        ),
    ]
