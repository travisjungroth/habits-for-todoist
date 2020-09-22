# Generated by Django 3.1.1 on 2020-09-09 01:18

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('days', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('completed', models.BooleanField(default=False)),
                ('date', models.DateField()),
                ('order', models.IntegerField()),
            ],
            options={
                'ordering': ['-date', 'order'],
            },
        ),
        migrations.CreateModel(
            name='TaskTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order')),
                ('name', models.CharField(max_length=255)),
                ('morning', models.BooleanField()),
                ('reminder_time', models.CharField(help_text='like 9pm', max_length=10)),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='todoer.schedule')),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
    ]
