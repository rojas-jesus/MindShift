# Generated by Django 4.2.6 on 2023-11-01 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_state_thoughtdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thoughtdate',
            name='date',
            field=models.DateField(),
        ),
    ]