# Generated by Django 4.2.7 on 2023-12-14 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartphone', '0006_alter_brand_created_at_alter_brand_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='brand',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
