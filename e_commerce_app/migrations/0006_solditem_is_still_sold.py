# Generated by Django 3.0.2 on 2020-01-24 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_commerce_app', '0005_auto_20200124_0110'),
    ]

    operations = [
        migrations.AddField(
            model_name='solditem',
            name='is_still_sold',
            field=models.BooleanField(default=True),
        ),
    ]
