# Generated by Django 4.2 on 2025-01-13 16:07

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("vacancy", "0005_alter_company_created_at_alter_vacancy_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="company",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2025, 1, 13, 16, 7, 49, 866949, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="vacancy",
            name="company",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="vacancies",
                to="vacancy.company",
            ),
        ),
        migrations.AlterField(
            model_name="vacancy",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2025, 1, 13, 16, 7, 49, 867329, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
