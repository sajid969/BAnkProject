# Generated by Django 2.2.13 on 2021-01-27 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheetupload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankdetails',
            name='ifsc',
            field=models.CharField(max_length=30),
        ),
    ]
