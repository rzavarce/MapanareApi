# Generated by Django 3.2.3 on 2021-06-09 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicles',
            old_name='engines_models',
            new_name='engine_model',
        ),
        migrations.RenameField(
            model_name='vehicles',
            old_name='engines_type',
            new_name='engine_type',
        ),
    ]
