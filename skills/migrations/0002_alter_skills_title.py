# Generated by Django 5.0.4 on 2024-04-22 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
