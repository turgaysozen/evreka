# Generated by Django 3.1.1 on 2020-09-28 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('collection_frequency', models.IntegerField()),
                ('last_collection', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('operation_date', models.DateField()),
                ('bin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collection.bin')),
            ],
        ),
    ]
