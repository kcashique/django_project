# Generated by Django 4.0.4 on 2022-05-13 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_country_state_delete_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='country',
            old_name='contry',
            new_name='country',
        ),
    ]
