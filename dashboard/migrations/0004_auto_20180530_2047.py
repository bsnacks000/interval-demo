# Generated by Django 2.0.5 on 2018-05-30 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20180530_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pump',
            name='pump',
            field=models.IntegerField(),
        ),
    ]
