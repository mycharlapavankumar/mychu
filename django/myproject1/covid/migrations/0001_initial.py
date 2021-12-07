# Generated by Django 3.1.2 on 2020-10-10 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=20)),
                ('p_age', models.IntegerField()),
                ('p_email', models.EmailField(max_length=254)),
            ],
        ),
    ]
