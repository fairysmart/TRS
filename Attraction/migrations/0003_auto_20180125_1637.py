# Generated by Django 2.0 on 2018-01-25 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Attraction', '0002_userattraction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userattraction',
            name='photoCount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='userattraction',
            name='rating',
            field=models.FloatField(null=True),
        ),
    ]