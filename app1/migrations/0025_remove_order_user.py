# Generated by Django 3.1.5 on 2021-01-31 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0024_auto_20210131_1759'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
    ]
