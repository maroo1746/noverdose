# Generated by Django 4.2.6 on 2023-10-18 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchmed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='med_list',
            name='contraindicated_info',
            field=models.CharField(blank=True, max_length=225),
        ),
    ]