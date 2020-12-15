# Generated by Django 3.1.3 on 2020-12-13 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20201213_2133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='position',
        ),
        migrations.AddField(
            model_name='player',
            name='position',
            field=models.ForeignKey(help_text='Select a position of player', null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.position'),
        ),
    ]
