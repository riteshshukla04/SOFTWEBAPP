# Generated by Django 2.2.14 on 2020-10-04 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_auto_20201003_0133'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='TimesBooked',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]