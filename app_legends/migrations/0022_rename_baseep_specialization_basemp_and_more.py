# Generated by Django 5.0.3 on 2024-04-04 13:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_legends', '0021_character_proficiency_characterexpertise_proficient'),
    ]

    operations = [
        migrations.RenameField(
            model_name='specialization',
            old_name='baseEP',
            new_name='baseMP',
        ),
        migrations.AddField(
            model_name='specialization',
            name='startingSpells',
            field=models.ManyToManyField(blank=True, to='app_legends.spell'),
        ),
        migrations.CreateModel(
            name='Armor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('armorType', models.CharField(choices=[('Leve', 'Leve'), ('Média', 'Média'), ('Pesada', 'Pesada')], default='Média', max_length=7)),
                ('description', models.TextField()),
                ('firstRequirementValue', models.IntegerField(blank=True, null=True)),
                ('secondRequirementValue', models.IntegerField(blank=True, null=True)),
                ('firstRequirement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='first_req', to='app_legends.expertise')),
                ('secondRequirement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='second_req', to='app_legends.expertise')),
            ],
            options={
                'ordering': ['armorType'],
            },
        ),
        migrations.AddField(
            model_name='specialization',
            name='startingArmor',
            field=models.ManyToManyField(blank=True, to='app_legends.armor'),
        ),
    ]
