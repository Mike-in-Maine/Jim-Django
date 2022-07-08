# Generated by Django 4.0.5 on 2022-07-01 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_item_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ABEPOID', models.CharField(max_length=255)),
                ('price', models.FloatField(max_length=24)),
                ('description', models.CharField(max_length=1024)),
                ('img_url', models.CharField(max_length=512)),
            ],
        ),
    ]