# Generated by Django 5.0.3 on 2024-05-26 13:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_legends', '0039_remove_characterweapon_modifier_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='armor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_legends.armor'),
        ),
        migrations.AlterField(
            model_name='character',
            name='magicGroup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_legends.magicgroup'),
        ),
        migrations.AlterField(
            model_name='characterweapon',
            name='modifier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_legends.modifier'),
        ),
    ]
