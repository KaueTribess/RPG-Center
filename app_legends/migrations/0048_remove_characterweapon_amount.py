# Generated by Django 5.0.3 on 2024-06-09 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_legends', '0047_alter_weapon_combatrange'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='characterweapon',
            name='amount',
        ),
    ]