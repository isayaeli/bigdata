# Generated by Django 4.0.6 on 2022-07-18 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bigdata', '0003_alter_life_expectancy_options_life_expectancy_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='life_expectancy',
            name='indicator_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
