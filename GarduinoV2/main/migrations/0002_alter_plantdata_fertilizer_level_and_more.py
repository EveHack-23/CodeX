# Generated by Django 4.1.5 on 2023-01-21 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantdata',
            name='fertilizer_level',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='plantdata',
            name='humidity',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='plantdata',
            name='led_intensity',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='plantdata',
            name='temp',
            field=models.FloatField(default=0.0),
        ),
    ]
