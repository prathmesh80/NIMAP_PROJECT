# Generated by Django 4.1.7 on 2023-03-26 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("password", models.CharField(max_length=255)),
            ],
        ),
    ]