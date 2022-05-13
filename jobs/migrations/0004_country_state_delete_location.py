# Generated by Django 4.0.4 on 2022-05-13 09:26

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('contry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applied_country', to='jobs.job')),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countris',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applied_state', to='jobs.job')),
            ],
            options={
                'verbose_name': 'State',
                'verbose_name_plural': 'states',
            },
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]
