# Generated by Django 2.2.24 on 2021-09-07 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maldini', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='productcode',
            field=models.CharField(max_length=225, null=True),
        ),
    ]
