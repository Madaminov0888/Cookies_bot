# Generated by Django 4.1 on 2022-09-22 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("variables", "0002_cakedescription_chat_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="total_num",
            name="num",
            field=models.CharField(default="", max_length=255),
        ),
    ]
