# Generated by Django 4.1 on 2022-09-22 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0007_cakedescription_cakes"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Cakes",
            new_name="Cake",
        ),
    ]