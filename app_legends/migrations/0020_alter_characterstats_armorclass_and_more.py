# Generated by Django 5.0.3 on 2024-03-21 13:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_legends', '0019_alter_specialization_healdice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characterstats',
            name='armorClass',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='characterstats',
            name='conhecimento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='conhecimento', to='app_legends.characterattribute'),
        ),
        migrations.AlterField(
            model_name='characterstats',
            name='corpo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='corpo', to='app_legends.characterattribute'),
        ),
        migrations.AlterField(
            model_name='characterstats',
            name='currentEP',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='characterstats',
            name='currentHP',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='characterstats',
            name='currentWeight',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='characterstats',
            name='destreza',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='destreza', to='app_legends.characterattribute'),
        ),
        migrations.AlterField(
            model_name='characterstats',
            name='maxEP',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='characterstats',
            name='maxHP',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='characterstats',
            name='maxWeight',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='characterstats',
            name='mente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mente', to='app_legends.characterattribute'),
        ),
        migrations.AlterField(
            model_name='characterstats',
            name='movement',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='characterstats',
            name='passivePerception',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='characterstats',
            name='social',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='social', to='app_legends.characterattribute'),
        ),
        migrations.AlterField(
            model_name='characterstats',
            name='weightStatus',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
