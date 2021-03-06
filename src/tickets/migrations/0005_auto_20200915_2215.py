# Generated by Django 3.0.7 on 2020-09-15 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0004_auto_20200915_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='journey_amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='total_amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
