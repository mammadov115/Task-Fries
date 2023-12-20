# Generated by Django 4.2.7 on 2023-11-28 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0004_alter_admin_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='')),
                ('description', models.TextField(verbose_name='')),
                ('customer', models.ManyToManyField(to='account.customer', verbose_name='')),
                ('owner', models.ManyToManyField(to='account.admin', verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Workspace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='')),
                ('field', models.CharField(max_length=50, verbose_name='')),
                ('colleague', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.colleague', verbose_name='')),
                ('owner', models.ManyToManyField(to='account.admin', verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='')),
                ('description', models.TextField(verbose_name='')),
                ('deadline', models.DateTimeField(verbose_name='')),
                ('file', models.FileField(upload_to=None, verbose_name='')),
                ('result', models.FileField(upload_to=None, verbose_name='')),
                ('in_progress', models.BooleanField(verbose_name='')),
                ('finishing', models.BooleanField(verbose_name='')),
                ('colleagues', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.colleague', verbose_name='')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.project', verbose_name='')),
                ('workspace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.workspace', verbose_name='')),
            ],
        ),
    ]