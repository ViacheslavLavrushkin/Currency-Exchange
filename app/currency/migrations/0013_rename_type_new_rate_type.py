# Generated by Django 3.2.3 on 2021-08-08 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0012_alter_rate_type_new'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rate',
            old_name='type_new',
            new_name='type',
        ),
    ]