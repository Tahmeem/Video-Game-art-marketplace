# Generated by Django 3.2.4 on 2021-06-26 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Art', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
