# Generated by Django 2.0 on 2018-01-24 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Photo', '0007_auto_20180124_1729'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='user_id',
            new_name='userName',
        ),
    ]
