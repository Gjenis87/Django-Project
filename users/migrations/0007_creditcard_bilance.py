# Generated by Django 4.1.7 on 2023-03-17 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_creditcard_credit_card_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditcard',
            name='bilance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
