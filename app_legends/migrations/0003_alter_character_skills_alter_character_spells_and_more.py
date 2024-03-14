# Generated by Django 5.0.3 on 2024-03-14 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_legends', '0002_alter_character_ilustration_alter_item_ilustration_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='skills',
            field=models.ManyToManyField(blank=True, to='app_legends.skill'),
        ),
        migrations.AlterField(
            model_name='character',
            name='spells',
            field=models.ManyToManyField(blank=True, to='app_legends.spell'),
        ),
        migrations.AlterField(
            model_name='characterattribute',
            name='expertises',
            field=models.ManyToManyField(blank=True, to='app_legends.characterexpertise'),
        ),
        migrations.AlterField(
            model_name='characterproficiencies',
            name='elements',
            field=models.ManyToManyField(blank=True, to='app_legends.magicelement'),
        ),
        migrations.AlterField(
            model_name='characterproficiencies',
            name='expertises',
            field=models.ManyToManyField(blank=True, to='app_legends.expertise'),
        ),
        migrations.AlterField(
            model_name='characterproficiencies',
            name='tools',
            field=models.ManyToManyField(blank=True, to='app_legends.item'),
        ),
        migrations.AlterField(
            model_name='characterproficiencies',
            name='weapons',
            field=models.ManyToManyField(blank=True, to='app_legends.weapontype'),
        ),
        migrations.AlterField(
            model_name='magicgroup',
            name='elements',
            field=models.ManyToManyField(blank=True, to='app_legends.magicelement'),
        ),
        migrations.AlterField(
            model_name='spell',
            name='elements',
            field=models.ManyToManyField(blank=True, to='app_legends.magicelement'),
        ),
        migrations.AlterField(
            model_name='spell',
            name='ingredientCost',
            field=models.ManyToManyField(blank=True, to='app_legends.item'),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='traits',
            field=models.ManyToManyField(blank=True, to='app_legends.weapontrait'),
        ),
    ]