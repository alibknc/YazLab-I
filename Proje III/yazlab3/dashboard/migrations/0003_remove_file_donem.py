# Generated by Django 3.2.9 on 2021-12-17 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_file_danisman'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='donem',
        ),
    ]
