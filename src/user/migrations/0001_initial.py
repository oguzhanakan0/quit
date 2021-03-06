# Generated by Django 3.1.6 on 2021-09-02 22:42

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=40, unique=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('first_joined', models.DateTimeField(blank=True, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('auth_source', models.IntegerField(choices=[(1, 'Google'), (2, 'Facebook'), (3, 'Apple'), (4, 'Email')])),
                ('is_info_complete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserConnection',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('verification_code', models.CharField(max_length=100, unique=True)),
                ('supporter_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('smoker', models.ForeignKey(db_column='smokerid', on_delete=django.db.models.deletion.PROTECT, related_name='+', to='user.user')),
                ('supporter', models.ForeignKey(blank=True, db_column='supporter_username', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='user.user', to_field='username')),
            ],
        ),
        migrations.CreateModel(
            name='SmokerSupporter',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_linked', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=False)),
                ('relationship', models.IntegerField(choices=[(1, 'Family'), (2, 'Friend'), (3, 'Colleague'), (4, 'Significant Other'), (5, 'Other')])),
                ('smoker', models.ForeignKey(db_column='smokerid', on_delete=django.db.models.deletion.PROTECT, related_name='+', to='user.user')),
                ('supporter', models.ForeignKey(db_column='supporterid', on_delete=django.db.models.deletion.PROTECT, related_name='+', to='user.user')),
            ],
        ),
    ]
