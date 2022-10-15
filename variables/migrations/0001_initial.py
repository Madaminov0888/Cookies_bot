# Generated by Django 4.1 on 2022-09-22 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CakeDescription",
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
                ("ids", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Total_num",
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
                ("chat_id", models.IntegerField(default=0)),
                ("num", models.IntegerField()),
            ],
        ),
    ]