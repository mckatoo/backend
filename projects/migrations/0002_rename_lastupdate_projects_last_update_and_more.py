# Generated by Django 5.0.4 on 2024-04-18 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='lastUpdate',
            new_name='last_update',
        ),
        migrations.RenameField(
            model_name='projects',
            old_name='repositoryLink',
            new_name='repository_link',
        ),
    ]
