# Generated by Django 4.0.6 on 2022-07-17 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Life_Expectance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=100)),
                ('country_code', models.CharField(max_length=100)),
                ('indicator_name', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
            ],
        ),
    ]
