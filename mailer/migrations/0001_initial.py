# Generated by Django 5.0.4 on 2024-04-29 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mailer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_from', models.CharField(db_column='from', max_length=300)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Messages',
                'db_table': 'Messages',
            },
        ),
    ]
