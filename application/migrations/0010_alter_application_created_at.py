# Generated by Django 4.2 on 2025-01-18 15:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0009_alter_application_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 18, 15, 58, 36, 1156, tzinfo=datetime.timezone.utc)),
        ),
    ]
