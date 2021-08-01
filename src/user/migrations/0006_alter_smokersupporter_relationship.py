# Generated by Django 3.2.4 on 2021-07-24 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_smokersupporter_user_userconnection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smokersupporter',
            name='relationship',
            field=models.IntegerField(choices=[(1, 'Family'), (2, 'Friend'), (3, 'Colleague'), (4, 'Significant Other'), (5, 'Other')]),
        ),
    ]
