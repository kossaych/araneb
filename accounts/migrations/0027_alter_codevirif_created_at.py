# Generated by Django 4.1.6 on 2023-02-18 09:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0026_alter_codevirif_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codevirif',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 18, 9, 33, 0, 995929, tzinfo=datetime.timezone.utc)),
        ),
    ]