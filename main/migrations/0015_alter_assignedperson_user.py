# Generated by Django 4.2.7 on 2023-12-23 21:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0014_alter_assignedpersonproxy_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignedperson',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]