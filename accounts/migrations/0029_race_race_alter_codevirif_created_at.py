# Generated by Django 4.1.6 on 2023-02-19 16:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0028_alter_codevirif_created_at_race'),
    ]

    operations = [
        migrations.AddField(
            model_name='race',
            name='Race',
            field=models.CharField(default='------', max_length=200),
        ),
        migrations.AlterField(
            model_name='codevirif',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 19, 16, 1, 16, 533891, tzinfo=datetime.timezone.utc)),
        ),
    ]
