# Generated by Django 3.1.7 on 2021-05-17 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_auto_20210517_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search_list',
            name='courseName',
            field=models.CharField(max_length=255),
        ),
    ]
