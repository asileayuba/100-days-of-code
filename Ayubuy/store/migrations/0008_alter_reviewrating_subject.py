# Generated by Django 5.1.7 on 2025-04-01 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0007_reviewrating"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reviewrating",
            name="subject",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
