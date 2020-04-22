# Generated by Django 3.0.5 on 2020-04-21 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Market', '0008_auto_20200421_0127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='address',
        ),
        migrations.AddField(
            model_name='address',
            name='Country',
            field=models.CharField(default='Canada', max_length=30),
        ),
        migrations.AddField(
            model_name='address',
            name='Zipcode',
            field=models.CharField(default='H1H 1H1', max_length=6),
        ),
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.CharField(default='Montreal', max_length=30),
        ),
        migrations.AddField(
            model_name='address',
            name='line_one',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='address',
            name='line_two',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='address',
            name='province',
            field=models.CharField(default='QC', max_length=30),
        ),
    ]