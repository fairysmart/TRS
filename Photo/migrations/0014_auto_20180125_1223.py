# Generated by Django 2.0 on 2018-01-25 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Photo', '0013_province_nameinfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='provinceId',
            field=models.IntegerField(null=True),
        ),
    ]
