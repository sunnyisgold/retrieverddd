# Generated by Django 3.0.6 on 2020-06-09 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='photo',
            new_name='photo_url',
        ),
        migrations.AddField(
            model_name='account',
            name='age',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
