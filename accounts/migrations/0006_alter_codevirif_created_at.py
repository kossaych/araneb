# Generated by Django 4.1.1 on 2022-10-30 14:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_codevirif_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codevirif',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 30, 14, 57, 31, 734905, tzinfo=datetime.timezone.utc)),
        ),
    ]
