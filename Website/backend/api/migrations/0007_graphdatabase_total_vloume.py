# Generated by Django 5.0.1 on 2024-02-17 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_graphdatabase_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='graphdatabase',
            name='total_vloume',
            field=models.FloatField(default=3.1),
        ),
    ]
