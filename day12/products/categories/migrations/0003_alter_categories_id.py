# Generated by Django 4.2.4 on 2023-08-11 01:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("categories", "0002_alter_categories_image_alter_categories_info"),
    ]

    operations = [
        migrations.AlterField(
            model_name="categories",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
