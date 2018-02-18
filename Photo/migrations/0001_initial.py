# Generated by Django 2.0 on 2018-01-24 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('photoId', models.AutoField(primary_key=True, serialize=False)),
                ('photoFlikerId', models.CharField(max_length=20)),
                ('user_id', models.CharField(max_length=255)),
                ('takenDate', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('pageURL', models.CharField(max_length=255)),
                ('downloadURL', models.CharField(max_length=255)),
                ('filePath', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('province', models.CharField(max_length=255)),
                ('isVideo', models.BooleanField()),
            ],
            options={
                'db_table': 'photo',
            },
        ),
    ]