# Generated by Django 5.0.3 on 2024-05-26 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_legends', '0043_rename_atackroll_characterweapon_attackroll'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weapon',
            old_name='range',
            new_name='shotRange',
        ),
        migrations.AddField(
            model_name='weapon',
            name='combatRange',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]