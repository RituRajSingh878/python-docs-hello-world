# Generated by Django 2.0.6 on 2018-10-13 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='found',
            name='Photo',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='lost',
            name='Photo',
            field=models.ImageField(upload_to=''),
        ),
    ]
