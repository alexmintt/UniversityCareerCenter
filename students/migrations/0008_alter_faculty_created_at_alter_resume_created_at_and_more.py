# Generated by Django 4.2 on 2025-01-13 15:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0007_alter_student_enrollment_year_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="faculty",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2025, 1, 13, 15, 55, 58, 245900, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="resume",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2025, 1, 13, 15, 55, 58, 246044, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2025, 1, 13, 15, 55, 58, 246307, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
