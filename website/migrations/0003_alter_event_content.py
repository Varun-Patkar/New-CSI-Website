# Generated by Django 3.2.9 on 2021-11-21 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_event_registrationlink'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='content',
            field=models.TextField(null=True),
        ),
    ]
