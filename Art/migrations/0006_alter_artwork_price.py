# Generated by Django 3.2.4 on 2021-07-11 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Art', '0005_auto_20210710_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='Price',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
