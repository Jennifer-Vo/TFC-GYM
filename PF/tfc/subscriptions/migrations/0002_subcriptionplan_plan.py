# Generated by Django 4.1.3 on 2022-11-09 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcriptionplan',
            name='plan',
            field=models.CharField(choices=[('Yearly', 'Yearly'), ('Monthly', 'Monthly')], default='x', max_length=100),
        ),
    ]
