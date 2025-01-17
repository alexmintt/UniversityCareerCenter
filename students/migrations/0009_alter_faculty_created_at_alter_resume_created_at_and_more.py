# Generated by Django 4.2 on 2025-01-13 16:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0008_alter_faculty_created_at_alter_resume_created_at_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="faculty",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2025, 1, 13, 16, 7, 49, 867530, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="resume",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2025, 1, 13, 16, 7, 49, 868137, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2025, 1, 13, 16, 7, 49, 868352, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
