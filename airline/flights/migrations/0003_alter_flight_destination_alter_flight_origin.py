# Generated by Django 4.1.3 on 2022-11-22 01:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("flights", "0002_airport"),
    ]

    operations = [
        migrations.AlterField(
            model_name="flight",
            name="destination",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="arrivals",
                to="flights.airport",
            ),
        ),
        migrations.AlterField(
            model_name="flight",
            name="origin",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="departures",
                to="flights.airport",
            ),
        ),
    ]
