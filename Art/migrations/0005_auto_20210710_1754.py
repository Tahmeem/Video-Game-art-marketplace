# Generated by Django 3.2.4 on 2021-07-10 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Art', '0004_auto_20210626_1932'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artwork',
            name='creator_IG',
        ),
        migrations.AlterField(
            model_name='artwork',
            name='Price',
            field=models.FloatField(),
        ),
    ]