# Generated by Django 2.1.5 on 2019-01-26 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scouts', '0002_scout_hatches_secured'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scout',
            options={'ordering': ['match_number']},
        ),
    ]
