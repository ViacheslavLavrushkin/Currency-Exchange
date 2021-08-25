# Generated by Django 3.2.3 on 2021-08-24 20:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='code_name',
            field=models.CharField(default=None, max_length=64, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='rate',
            name='bank',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='currency.bank'),  # noqa
        ),
    ]
