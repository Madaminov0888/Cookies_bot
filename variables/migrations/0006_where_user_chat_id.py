# Generated by Django 4.1 on 2022-09-26 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("variables", "0005_where_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="where_user",
            name="chat_id",
            field=models.IntegerField(default=0),
        ),
    ]
