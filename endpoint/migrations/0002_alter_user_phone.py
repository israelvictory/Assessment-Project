# Generated by Django 3.2.4 on 2021-06-26 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endpoint', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]