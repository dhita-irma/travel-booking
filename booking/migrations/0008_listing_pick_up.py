# Generated by Django 3.1.1 on 2020-11-05 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_auto_20201105_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='pick_up',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
