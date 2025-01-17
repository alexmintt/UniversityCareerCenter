# Generated by Django 4.2 on 2025-01-13 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0005_resume_alter_student_resume"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="faculty",
            options={
                "ordering": ["name"],
                "verbose_name": "Факультет",
                "verbose_name_plural": "Факультеты",
            },
        ),
        migrations.AlterModelOptions(
            name="resume",
            options={
                "ordering": ["title"],
                "verbose_name": "Резюме",
                "verbose_name_plural": "Резюме",
            },
        ),
        migrations.AlterModelOptions(
            name="student",
            options={
                "ordering": ["name"],
                "verbose_name": "Студент",
                "verbose_name_plural": "Студенты",
            },
        ),
        migrations.AlterField(
            model_name="student",
            name="faculty",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="students.faculty",
            ),
        ),
    ]
