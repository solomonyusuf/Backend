# Generated by Django 2.2.24 on 2021-09-06 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TrippleG', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=225)),
                ('phoneNumber', models.CharField(max_length=225)),
                ('email', models.CharField(max_length=225)),
                ('message', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='')),
                ('title', models.CharField(max_length=225)),
                ('body', models.CharField(max_length=2000)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='contact1',
        ),
        migrations.DeleteModel(
            name='News1',
        ),
    ]
