# Generated by Django 5.0.3 on 2024-03-18 12:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_legends', '0009_characterattribute_remaining'),
    ]

    operations = [
        migrations.AddField(
            model_name='race',
            name='age',
            field=models.TextField(default='Tantos anos'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='race',
            name='attributeIncrease1',
            field=models.CharField(choices=[('Corpo', 'Corpo'), ('Destreza', 'Destreza'), ('Conhecimento', 'Conhecimento'), ('Mente', 'Mente'), ('Social', 'Social')], default='Corpo', max_length=12),
        ),
        migrations.AddField(
            model_name='race',
            name='attributeIncrease2',
            field=models.CharField(blank=True, choices=[('Corpo', 'Corpo'), ('Destreza', 'Destreza'), ('Conhecimento', 'Conhecimento'), ('Mente', 'Mente'), ('Social', 'Social')], max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='race',
            name='attributeIncreaseValue1',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='race',
            name='attributeIncreaseValue2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='race',
            name='baseMovement',
            field=models.FloatField(default=9.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='race',
            name='bodyType',
            field=models.CharField(choices=[('Pequeno', 'Pequeno'), ('Normal', 'Normal'), ('Grande', 'Grande')], default='Normal', max_length=7),
        ),
        migrations.AddField(
            model_name='race',
            name='height',
            field=models.TextField(default='Essa altura'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='race',
            name='magicAffinity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_legends.magicgroup'),
        ),
        migrations.AddField(
            model_name='race',
            name='title',
            field=models.CharField(default='titulo', max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
