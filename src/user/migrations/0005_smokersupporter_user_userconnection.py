# Generated by Django 3.2.4 on 2021-07-24 23:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0004_auto_20210725_0229'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserConnection',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False)),
                ('verification_code', models.CharField(max_length=100, unique=True)),
                ('supporter_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('smokerid', models.ForeignKey(db_column='smokerid', on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('supporter', models.ForeignKey(blank=True, db_column='supporter_username', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField()),
                ('auth_source', models.IntegerField(choices=[(1, 'Google'), (2, 'Facebook'), (3, 'Apple'), (4, 'Email')])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SmokerSupporter',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False)),
                ('date_linked', models.DateField()),
                ('is_active', models.BooleanField(default=False)),
                ('relationship', models.IntegerField(choices=[(1, 'Family'), (2, 'Friend'), (3, 'Colleague'), (4, 'Significant Other')])),
                ('smokerid', models.ForeignKey(db_column='smokerid', on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('supporterid', models.ForeignKey(db_column='supporterid', on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]