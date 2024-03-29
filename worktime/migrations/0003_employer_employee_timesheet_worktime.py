# Generated by Django 5.0.1 on 2024-02-08 15:31

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worktime', '0002_alter_customuser_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Работодатель')),
                ('joined', models.DateTimeField(auto_now_add=True)),
                ('customuser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Работник')),
                ('engaged', models.DateTimeField(default=django.utils.timezone.now)),
                ('customuser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='employee', to=settings.AUTH_USER_MODEL)),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worktime.employer')),
            ],
            options={
                'unique_together': {('name', 'customuser')},
            },
        ),
        migrations.CreateModel(
            name='Timesheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_work', models.BooleanField(choices=[(True, 'WORK'), (False, 'NOWORK')], default=False, verbose_name='Статус работы')),
                ('datetime_start', models.DateTimeField(blank=True, null=True, verbose_name='Начало рабочего дня')),
                ('datetime_complete', models.DateTimeField(blank=True, null=True, verbose_name='Конец рабочего дня')),
                ('time_break', models.DateTimeField(auto_now=True, null=True, verbose_name='Начало перерыва')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='timesheet', to='worktime.employee')),
            ],
            options={
                'verbose_name_plural': 'Таймшиты',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='WorkTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_break_safe_sheets', models.DateTimeField(blank=True, null=True, verbose_name='Запись начала перерыва')),
                ('end_break_safe_sheets', models.DateTimeField(blank=True, null=True, verbose_name='Запись начала перерыва')),
                ('time_worked_per_day', models.TimeField(blank=True, null=True)),
                ('timesheet', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='worktime', to='worktime.timesheet')),
            ],
        ),
    ]
