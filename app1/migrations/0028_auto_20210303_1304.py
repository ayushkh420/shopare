# Generated by Django 3.1.7 on 2021-03-03 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0027_order_payment_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_choice',
            field=models.CharField(choices=[('cash_on_delivery', 'Cash on delivery'), ('take_away', 'Take away')], default=1, max_length=30),
        ),
    ]
