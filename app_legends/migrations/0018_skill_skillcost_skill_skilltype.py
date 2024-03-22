# Generated by Django 5.0.3 on 2024-03-21 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_legends', '0017_alter_specialization_baseep_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='skillCost',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='skill',
            name='skillType',
            field=models.CharField(choices=[('Passiva', 'Passiva'), ('Ativa', 'Ativa')], default='Passiva', max_length=7),
        ),
    ]
