# Generated by Django 2.0.7 on 2018-08-29 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingest', '0015_add_processed_boolean'),
    ]

    operations = [
        migrations.AddField(
            model_name='committee',
            name='location_tz',
            field=models.CharField(default='America/Los_Angeles', max_length=255),
        ),
    ]
