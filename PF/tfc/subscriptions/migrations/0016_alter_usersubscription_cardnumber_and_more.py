# Generated by Django 4.1.3 on 2022-12-13 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0015_alter_usersubscription_expiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersubscription',
            name='cardnumber',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='usersubscription',
            name='cvv',
            field=models.CharField(max_length=100),
        ),
    ]