# Generated by Django 4.0.5 on 2022-07-01 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_rename_description_orders_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='condition',
            field=models.CharField(default=0, max_length=24),
            preserve_default=False,
        ),
    ]
