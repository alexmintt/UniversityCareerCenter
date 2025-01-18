# Generated by Django 4.2 on 2025-01-18 16:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0014_alter_faculty_created_at_alter_resume_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='certificates/')),
                ('issued_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='resume',
            name='portfolio_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 18, 16, 54, 44, 441594, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='resume',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 18, 16, 54, 44, 441867, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='student',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 18, 16, 54, 44, 442384, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='resume',
            name='certificates',
            field=models.ManyToManyField(blank=True, related_name='resumes', to='students.certificate'),
        ),
    ]
