# Generated by Django 3.1.1 on 2020-10-28 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_category_destination_listing'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='price',
            field=models.DecimalField(decimal_places=0, default=99999, max_digits=12),
        ),
    ]
