# Generated by Django 4.1.6 on 2023-02-19 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0028_alter_codevirif_created_at_race'),
        ('lapinproduction', '0009_vaccinlapin_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lapinproduction',
            name='race',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.race'),
        ),
    ]
