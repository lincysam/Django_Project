# Generated by Django 4.2.7 on 2023-12-14 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smartphone', '0005_alter_mobile_trans_trans_model_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='created_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='brand',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='mobile_trans',
            name='trans_model',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='phonemodel', to='smartphone.phonemodel'),
        ),
    ]
