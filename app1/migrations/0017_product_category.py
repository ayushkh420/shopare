# Generated by Django 3.1.5 on 2021-01-30 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0016_remove_product_product_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app1.category'),
        ),
    ]
