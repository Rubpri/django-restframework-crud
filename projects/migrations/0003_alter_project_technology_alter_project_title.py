# Generated by Django 5.0.2 on 2024-02-08 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_rename_created_att_project_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='technology',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]
