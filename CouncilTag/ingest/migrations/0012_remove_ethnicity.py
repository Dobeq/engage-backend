# Generated by Django 2.0.7 on 2018-08-17 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ingest', '0011_cutoff_days_may_be_negative'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='ethnicity',
        ),
    ]
