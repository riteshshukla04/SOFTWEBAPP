# Generated by Django 2.2.14 on 2020-10-02 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20201003_0131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='type',
            field=models.CharField(choices=[('Electricity', 'Electricity'), ('HouseKeeping', 'HouseKeeping'), ('PestControl', 'PestControl'), ('Carpenter', 'Carpenter'), ('Milk', 'Milk'), ('Civil', 'Civil'), ('Newspaper', 'Newspaper'), ('Plumber', 'Plumber')], max_length=200, null=True),
        ),
    ]
