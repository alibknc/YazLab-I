# Generated by Django 3.2.9 on 2021-12-17 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_alter_file_ozet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='hocaID',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
