# Generated by Django 4.0 on 2021-12-27 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='category',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
