# Generated by Django 3.2.9 on 2022-01-28 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20220126_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='first_name',
            field=models.CharField(default='_amon', max_length=255),
        ),
    ]
