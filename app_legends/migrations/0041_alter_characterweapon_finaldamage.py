# Generated by Django 5.0.3 on 2024-05-26 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_legends', '0040_alter_character_armor_alter_character_magicgroup_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characterweapon',
            name='finalDamage',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
