# Generated by Django 2.0 on 2018-01-25 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Photo', '0015_province_pingyingname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='province',
            name='pingyingName',
            field=models.CharField(max_length=255),
        ),
    ]
