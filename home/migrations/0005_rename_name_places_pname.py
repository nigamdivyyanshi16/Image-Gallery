# Generated by Django 4.2.5 on 2023-09-27 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_places'),
    ]

    operations = [
        migrations.RenameField(
            model_name='places',
            old_name='name',
            new_name='pname',
        ),
    ]
