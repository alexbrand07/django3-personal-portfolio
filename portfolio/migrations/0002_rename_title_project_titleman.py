# Generated by Django 3.2.5 on 2021-08-04 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='title',
            new_name='titleman',
        ),
    ]
