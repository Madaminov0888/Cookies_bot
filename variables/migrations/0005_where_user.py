# Generated by Django 4.1 on 2022-09-26 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("variables", "0004_going_to_order"),
    ]

    operations = [
        migrations.CreateModel(
            name="Where_User",
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
                ("location", models.CharField(max_length=255)),
            ],
        ),
    ]
