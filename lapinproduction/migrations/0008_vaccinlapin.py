# Generated by Django 3.2.16 on 2023-02-04 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lapinproduction', '0007_groupeproduction_create_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='VaccinLapin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_vaccin', models.DateField(blank=True, null=True)),
                ('nom', models.CharField(blank=True, max_length=50, null=True)),
                ('prix', models.IntegerField(blank=True, null=True)),
                ('maladie', models.CharField(choices=[('La gale', 'La gale'), ('La teigne', 'La teigne'), ('Les mycoses', 'Les mycoses'), ('La myxomatose', 'La myxomatose'), ('Le coryza', 'Le coryza')], default='non_vérifié', max_length=200)),
                ('lapin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lapinproduction.lapinproduction')),
            ],
        ),
    ]
