# Generated by Django 3.1.5 on 2021-01-29 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_auto_20210122_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='productbakery',
            name='product_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='productgrocery',
            name='product_id',
            field=models.IntegerField(default=0),
        ),
    ]