# Generated by Django 4.0.4 on 2022-05-13 09:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0007_remove_country_created_remove_country_is_active_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='state',
            options={'verbose_name': 'State', 'verbose_name_plural': 'States'},
        ),
        migrations.RenameField(
            model_name='state',
            old_name='state',
            new_name='name',
        ),
        migrations.AddField(
            model_name='country',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='country',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='country',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='country',
            name='id',
            field=models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
