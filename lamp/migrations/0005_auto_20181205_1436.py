# Generated by Django 2.1.3 on 2018-12-05 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lamp', '0004_rotations'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bright',
            old_name='value',
            new_name='bright',
        ),
    ]
