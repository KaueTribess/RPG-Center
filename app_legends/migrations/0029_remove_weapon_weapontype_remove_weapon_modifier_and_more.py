# Generated by Django 5.0.3 on 2024-04-27 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_legends', '0028_alter_spell_areaofeffect_alter_spell_range'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weapon',
            name='weaponType',
        ),
        migrations.RemoveField(
            model_name='weapon',
            name='Modifier',
        ),
        migrations.AddField(
            model_name='character',
            name='crowns',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='cost',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='modifier',
            name='cost',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='modifier',
            name='traitsAdded',
            field=models.ManyToManyField(blank=True, to='app_legends.weapontrait'),
        ),
        migrations.AddField(
            model_name='modifier',
            name='type',
            field=models.CharField(choices=[('Passivo', 'Passivo'), ('Ativo', 'Ativo')], default='Passivo', max_length=7),
        ),
        migrations.AddField(
            model_name='weapon',
            name='cost',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='weapon',
            name='modifiers',
            field=models.ManyToManyField(blank=True, to='app_legends.modifier'),
        ),
        migrations.AddField(
            model_name='weapon',
            name='rarity',
            field=models.CharField(choices=[('Comum', 'Comum'), ('Especial', 'Especial')], default='Comum', max_length=8),
        ),
        migrations.AddField(
            model_name='weapon',
            name='type',
            field=models.CharField(choices=[('Simples', 'Simples'), ('Avançada', 'Avançada')], default='Simples', max_length=8),
        ),
        migrations.AlterField(
            model_name='characterproficiencies',
            name='weapons',
            field=models.ManyToManyField(blank=True, to='app_legends.weapon'),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='range',
            field=models.CharField(choices=[('Combate', 'Combate'), ('Precisão', 'Precisão')], default='Combate', max_length=8),
        ),
        migrations.DeleteModel(
            name='Wallet',
        ),
        migrations.DeleteModel(
            name='WeaponType',
        ),
    ]
