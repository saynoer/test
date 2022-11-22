# Generated by Django 4.1.3 on 2022-11-22 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("flights", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Airport",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.CharField(max_length=3)),
                ("city", models.CharField(max_length=64)),
            ],
        ),
    ]
