# Generated by Django 3.2.3 on 2021-06-14 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0003_auto_20210614_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicles',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Status'),
        ),
    ]
