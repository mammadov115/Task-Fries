# Generated by Django 4.2.7 on 2023-12-19 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_task_file_alter_task_result'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='category',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.taskcategory'),
        ),
    ]
