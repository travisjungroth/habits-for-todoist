# Generated by Django 3.1.2 on 2020-10-26 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0002_remove_task_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='habit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='habits.habit'),
        ),
    ]
