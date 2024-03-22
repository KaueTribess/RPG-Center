# Generated by Django 5.0.3 on 2024-03-21 12:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_legends', '0014_character_armorclass_character_movement'),
    ]

    operations = [
        migrations.RenameField(
            model_name='characterstats',
            old_name='mana',
            new_name='maxEP',
        ),
        migrations.RenameField(
            model_name='characterstats',
            old_name='health',
            new_name='maxHP',
        ),
        migrations.RemoveField(
            model_name='character',
            name='armorClass',
        ),
        migrations.RemoveField(
            model_name='character',
            name='currentEP',
        ),
        migrations.RemoveField(
            model_name='character',
            name='currentHP',
        ),
        migrations.RemoveField(
            model_name='character',
            name='maxEP',
        ),
        migrations.RemoveField(
            model_name='character',
            name='maxHP',
        ),
        migrations.RemoveField(
            model_name='character',
            name='movement',
        ),
        migrations.RemoveField(
            model_name='characterstats',
            name='atributes',
        ),
        migrations.AddField(
            model_name='characterstats',
            name='conhecimento',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='conhecimento', to='app_legends.characterattribute'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='characterstats',
            name='corpo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='corpo', to='app_legends.characterattribute'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='characterstats',
            name='currentEP',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='characterstats',
            name='currentHP',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='characterstats',
            name='destreza',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='destreza', to='app_legends.characterattribute'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='characterstats',
            name='mente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='mente', to='app_legends.characterattribute'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='characterstats',
            name='social',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='social', to='app_legends.characterattribute'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specialization',
            name='baseEP',
            field=models.CharField(default=5, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specialization',
            name='baseHP',
            field=models.CharField(default=7, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specialization',
            name='expertiseAmout',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specialization',
            name='expertises',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app_legends.expertise'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specialization',
            name='healDice',
            field=models.CharField(default='1', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specialization',
            name='levelHP',
            field=models.CharField(default='1', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specialization',
            name='requiredElement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_legends.magicelement'),
        ),
        migrations.AddField(
            model_name='specialization',
            name='requiredMagicGroup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_legends.magicgroup'),
        ),
        migrations.AddField(
            model_name='specialization',
            name='startingMoney',
            field=models.CharField(default='1', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specialization',
            name='startingSkill',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app_legends.skill'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specialization',
            name='startingTools',
            field=models.ManyToManyField(blank=True, to='app_legends.item'),
        ),
        migrations.AddField(
            model_name='specialization',
            name='startingWeapons',
            field=models.ManyToManyField(blank=True, to='app_legends.weapon'),
        ),
    ]