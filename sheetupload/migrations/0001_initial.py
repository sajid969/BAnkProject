# Generated by Django 2.2.13 on 2021-01-27 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BankDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ifsc', models.FileField(max_length=30, upload_to='')),
                ('bank_id', models.IntegerField(blank=True)),
                ('branch', models.CharField(blank=True, max_length=100)),
                ('address', models.TextField(blank=True, max_length=256)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('district', models.CharField(blank=True, max_length=100)),
                ('state', models.CharField(blank=True, max_length=100)),
                ('bank_name', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
