# Generated by Django 4.2 on 2024-12-05 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=64, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('url', models.CharField(max_length=255)),
            ],
        ),
    ]
