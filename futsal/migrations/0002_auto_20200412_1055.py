# Generated by Django 3.0.4 on 2020-04-12 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('futsal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='contact',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='booking',
            name='booked_futsal',
            field=models.CharField(max_length=40),
        ),
    ]