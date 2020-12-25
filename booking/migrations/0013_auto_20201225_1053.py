# Generated by Django 3.1.1 on 2020-12-25 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0012_auto_20201121_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='image_url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='reservation_date',
            field=models.DateField(),
        ),
    ]