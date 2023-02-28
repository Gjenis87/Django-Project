# Generated by Django 4.1.7 on 2023-02-21 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('price', models.FloatField()),
                ('barcode', models.CharField(max_length=10)),
                ('expiry_date', models.DateTimeField()),
                ('quantity', models.IntegerField()),
                ('tag', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
    ]