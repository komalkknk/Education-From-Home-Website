# Generated by Django 3.1.7 on 2021-05-17 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_auto_20210517_1704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='search_list',
            name='title',
        ),
        migrations.AddField(
            model_name='search_list',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
