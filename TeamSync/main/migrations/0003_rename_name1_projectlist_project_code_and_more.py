# Generated by Django 5.0.1 on 2024-03-06 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_project_history_project_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectlist',
            old_name='name1',
            new_name='project_code',
        ),
        migrations.RenameField(
            model_name='projectlist',
            old_name='name',
            new_name='project_name',
        ),
        migrations.RemoveField(
            model_name='project_history',
            name='project_code',
        ),
    ]