# Generated by Django 4.1.5 on 2023-03-01 09:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0005_alter_estimation_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estimation',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 1, 9, 23, 13, 399705, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='estimation',
            name='waterfront',
            field=models.IntegerField(choices=[(1, 'oui'), (0, 'non')]),
        ),
        migrations.AlterField(
            model_name='estimation',
            name='zipcode',
            field=models.IntegerField(choices=[(98178, '98178'), (98125, '98125'), (98028, '98028'), (98136, '98136'), (98074, '98074'), (98053, '98053'), (98003, '98003'), (98198, '98198'), (98146, '98146'), (98038, '98038'), (98007, '98007'), (98115, '98115'), (98107, '98107'), (98126, '98126'), (98019, '98019'), (98103, '98103'), (98002, '98002'), (98133, '98133'), (98040, '98040'), (98092, '98092'), (98030, '98030'), (98119, '98119'), (98112, '98112'), (98052, '98052'), (98027, '98027'), (98117, '98117'), (98058, '98058'), (98001, '98001'), (98056, '98056'), (98166, '98166'), (98023, '98023'), (98070, '98070'), (98148, '98148'), (98105, '98105'), (98042, '98042'), (98008, '98008'), (98059, '98059'), (98122, '98122'), (98144, '98144'), (98004, '98004'), (98005, '98005'), (98034, '98034'), (98075, '98075'), (98116, '98116'), (98010, '98010'), (98118, '98118'), (98199, '98199'), (98032, '98032'), (98045, '98045'), (98102, '98102'), (98077, '98077'), (98108, '98108'), (98168, '98168'), (98177, '98177'), (98065, '98065'), (98029, '98029'), (98006, '98006'), (98109, '98109'), (98022, '98022'), (98033, '98033'), (98155, '98155'), (98024, '98024'), (98011, '98011'), (98031, '98031'), (98106, '98106'), (98072, '98072'), (98188, '98188'), (98014, '98014'), (98055, '98055'), (98039, '98039')]),
        ),
    ]
