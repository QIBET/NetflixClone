# Generated by Django 3.2.5 on 2021-07-21 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netflix', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='overview',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster_path',
            field=models.CharField(max_length=1000),
        ),
    ]
