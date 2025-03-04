# Generated by Django 4.1.7 on 2023-04-04 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0012_alter_product_price_sale"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="price_sale",
            field=models.DecimalField(
                blank=True, decimal_places=2, default=None, max_digits=6, null=True
            ),
        ),
    ]
