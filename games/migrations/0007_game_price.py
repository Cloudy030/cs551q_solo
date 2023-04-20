# Generated by Django 4.1.2 on 2023-04-20 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0006_cart_customer_order_lineitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
            preserve_default=False,
        ),
    ]