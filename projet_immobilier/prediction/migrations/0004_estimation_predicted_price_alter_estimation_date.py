# Generated by Django 4.1.5 on 2023-02-28 10:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0003_alter_estimation_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='estimation',
            name='predicted_price',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='estimation',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 28, 10, 12, 58, 245049, tzinfo=datetime.timezone.utc)),
        ),
    ]
