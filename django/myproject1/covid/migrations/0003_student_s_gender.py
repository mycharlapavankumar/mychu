# Generated by Django 3.1.2 on 2020-10-11 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0002_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='s_gender',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]