# Generated by Django 5.0.3 on 2024-04-10 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_legends', '0024_spellorigin_remove_spell_elements_spell_firstelement_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='spell',
            name='spellTier',
            field=models.CharField(choices=[('Simples', 'Simples'), ('Intermediária', 'Intermediária'), ('Avançada', 'Avançada')], default='Simples', max_length=13),
        ),
        migrations.AlterField(
            model_name='spell',
            name='spellType',
            field=models.CharField(choices=[('Encantamento', 'Encantamento'), ('Feitiço', 'Feitiço'), ('Conjuração', 'Conjuração'), ('Ritual', 'Ritual')], default='Feitiço', max_length=12),
        ),
    ]