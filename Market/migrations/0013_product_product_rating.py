# Generated by Django 2.0.7 on 2020-04-22 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Market', '0012_product_product_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_rating',
            field=models.IntegerField(default=0),
        ),
    ]