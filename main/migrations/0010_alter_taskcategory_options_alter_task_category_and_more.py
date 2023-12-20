# Generated by Django 4.2.7 on 2023-12-20 17:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0009_task_task_priority'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='taskcategory',
            options={'verbose_name_plural': 'Task Categories'},
        ),
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.taskcategory'),
        ),
        migrations.AlterField(
            model_name='task',
            name='users',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]