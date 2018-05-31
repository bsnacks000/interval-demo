# Generated by Django 2.0.5 on 2018-05-31 04:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20180530_2047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='building',
            name='id',
        ),
        migrations.AlterField(
            model_name='boiler',
            name='bdbid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boilers', to='dashboard.Building'),
        ),
        migrations.AlterField(
            model_name='building',
            name='bdbid',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='pump',
            name='bdbid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pumps', to='dashboard.Building'),
        ),
    ]