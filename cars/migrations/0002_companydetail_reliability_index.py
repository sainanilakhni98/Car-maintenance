# Generated by Django 3.0 on 2020-01-16 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='companydetail',
            name='reliability_index',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
