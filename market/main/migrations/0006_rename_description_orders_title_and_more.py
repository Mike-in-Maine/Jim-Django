# Generated by Django 4.0.5 on 2022-07-01 13:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_orders'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='description',
            new_name='TITLE',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='img_url',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='price',
        ),
        migrations.AddField(
            model_name='orders',
            name='ISBN',
            field=models.CharField(default=django.utils.timezone.now, max_length=24),
            preserve_default=False,
        ),
    ]
