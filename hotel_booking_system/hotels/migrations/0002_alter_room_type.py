# Generated by Django 5.1b1 on 2024-07-18 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='type',
            field=models.CharField(choices=[('SINGLE', 'Single'), ('DOUBLE', 'Double')], default='SINGLE', max_length=10),
        ),
    ]
