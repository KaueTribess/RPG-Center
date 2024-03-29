# Generated by Django 5.0.3 on 2024-03-14 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_legends', '0003_alter_character_skills_alter_character_spells_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='character',
            name='createdAt',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='lore',
            field=models.TextField(blank=True),
        ),
    ]
