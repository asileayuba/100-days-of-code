# Generated by Django 5.1.7 on 2025-03-21 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("category", "0003_auto_20250311_1821"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
