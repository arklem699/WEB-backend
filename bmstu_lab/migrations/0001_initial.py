# Generated by Django 4.2.4 on 2023-12-03 20:07

import bmstu_lab.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email адрес')),
                ('username', models.CharField(blank=True, max_length=30, null=True, unique=True, verbose_name='Имя пользователя')),
                ('password', models.CharField(max_length=100, verbose_name='Пароль')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Является ли пользователь менеджером?')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Является ли пользователь админом?')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='custom_user_groups', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='custom_user_permissions', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'customUser',
                'managed': True,
            },
            managers=[
                ('objects', bmstu_lab.models.NewUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('time', models.TimeField(blank=True, null=True)),
                ('doctor', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(blank=True, max_length=50, null=True)),
                ('image', models.BinaryField(blank=True, null=True)),
            ],
            options={
                'db_table': 'appointment',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creating', models.DateField(blank=True, null=True)),
                ('date_formation', models.DateField(blank=True, null=True)),
                ('date_completion', models.DateField(blank=True, null=True)),
                ('moderator', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(blank=True, max_length=50, null=True)),
                ('id_user', models.ForeignKey(db_column='id_user', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'application',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='AppApp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_appl', models.ForeignKey(db_column='id_appl', on_delete=django.db.models.deletion.CASCADE, to='bmstu_lab.application')),
                ('id_appoint', models.ForeignKey(db_column='id_appoint', on_delete=django.db.models.deletion.CASCADE, to='bmstu_lab.appointment')),
            ],
            options={
                'db_table': 'app_app',
                'managed': True,
            },
        ),
    ]
