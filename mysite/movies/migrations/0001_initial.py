# Generated by Django 5.0.4 on 2024-06-23 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Moviedate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('duration', models.FloatField()),
                ('rating', models.FloatField()),
                ('released', models.FloatField()),
            ],
        ),
    ]
