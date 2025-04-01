# Generated by Django 5.1.7 on 2025-04-01 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0004_alter_order_status_remove_orderproduct_variation_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="orderproduct",
            old_name="Payment",
            new_name="payment",
        ),
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("Cancelled", "Cancelled"),
                    ("Accepted", "Accepted"),
                    ("New", "New"),
                    ("Completed", "Completed"),
                ],
                default="New",
                max_length=10,
            ),
        ),
    ]
