# Generated by Django 3.0.7 on 2020-09-17 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leg', '0003_leg_cancelled_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='leg',
            name='available_seats',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='leg',
            name='day',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='leg',
            name='sold_seats',
            field=models.PositiveIntegerField(null=True),
        ),
    ]