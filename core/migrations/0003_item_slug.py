# Generated by Django 2.2 on 2020-07-13 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200710_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(default='test product'),
            preserve_default=False,
        ),
    ]
