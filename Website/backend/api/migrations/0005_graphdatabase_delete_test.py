# Generated by Django 5.0.1 on 2024-02-14 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_test_array'),
    ]

    operations = [
        migrations.CreateModel(
            name='GraphDatabase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_id', models.IntegerField()),
                ('p_id', models.IntegerField()),
                ('p_name', models.CharField(max_length=50)),
                ('time_array', models.JSONField()),
                ('volume_array', models.JSONField()),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='test',
        ),
    ]
