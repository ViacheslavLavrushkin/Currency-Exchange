# Generated by Django 3.2.3 on 2021-08-06 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0008_alter_rate_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='type_new',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Dollar'), (1, 'Euro')], default=100),
        ),
        migrations.AlterField(
            model_name='rate',
            name='type',
            field=models.CharField(max_length=5),
        ),
    ]
