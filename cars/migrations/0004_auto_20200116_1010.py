# Generated by Django 3.0 on 2020-01-16 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_companydetail_average_maintenance_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companydetail',
            name='four_Brake_oil',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='companydetail',
            name='six_Brake_oil',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='companydetail',
            name='six_air_filter',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='companydetail',
            name='six_fuel_filter',
            field=models.FloatField(),
        ),
    ]
