# Generated by Django 3.1.2 on 2020-10-01 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20201001_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complain',
            name='complain',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='complain',
            name='department',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='complain',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]