# Generated by Django 5.1.7 on 2025-03-29 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("Accepted", "Accepted"),
                    ("Completed", "Completed"),
                    ("Cancelled", "Cancelled"),
                    ("New", "New"),
                ],
                default="New",
                max_length=10,
            ),
        ),
    ]
