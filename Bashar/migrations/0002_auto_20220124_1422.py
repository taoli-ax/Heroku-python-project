# Generated by Django 3.1 on 2022-01-24 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bashar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipper',
            name='image',
            field=models.FilePathField(verbose_name='.r/img'),
        ),
    ]
