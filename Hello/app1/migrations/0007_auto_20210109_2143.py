# Generated by Django 3.1.2 on 2021-01-09 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_product_grocery'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='ProductGrocery',
        ),
    ]
