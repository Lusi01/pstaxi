# Generated by Django 3.2 on 2021-04-29 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motorpool', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='title',
            field=models.CharField(max_length=103),
        ),
    ]