# Generated by Django 3.2.9 on 2021-12-17 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_alter_file_hocaid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='hocaID',
            field=models.IntegerField(null=True),
        ),
    ]