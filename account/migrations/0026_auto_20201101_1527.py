# Generated by Django 2.2.14 on 2020-11-01 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0025_remove_customer_premium'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='Authenticated',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
