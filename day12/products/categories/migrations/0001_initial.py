# Generated by Django 4.2.4 on 2023-08-09 22:42

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Categories",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("info", models.TextField()),
                ("image", models.ImageField(null=True, upload_to="categories/images")),
            ],
        ),
    ]
