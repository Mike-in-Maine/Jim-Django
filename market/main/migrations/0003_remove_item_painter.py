# Generated by Django 4.0.5 on 2022-06-20 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_item_painter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='painter',
        ),
    ]
