# Generated by Django 2.2.1 on 2020-03-03 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uaccounts', '0003_allnotifications'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allnotifications',
            name='times_ago',
        ),
    ]
