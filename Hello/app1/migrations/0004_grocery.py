# Generated by Django 3.1.2 on 2021-01-09 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grocery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Store_name', models.CharField(max_length=50)),
            ],
        ),
    ]
