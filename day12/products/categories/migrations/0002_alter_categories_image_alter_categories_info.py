# Generated by Django 4.2.4 on 2023-08-10 22:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("categories", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="categories",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="categories/images"
            ),
        ),
        migrations.AlterField(
            model_name="categories",
            name="info",
            field=models.TextField(blank=True, null=True),
        ),
    ]
