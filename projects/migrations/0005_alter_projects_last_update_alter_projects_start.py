# Generated by Django 5.0.4 on 2024-05-07 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_projects_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='last_update',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='start',
            field=models.DateField(auto_now_add=True),
        ),
    ]