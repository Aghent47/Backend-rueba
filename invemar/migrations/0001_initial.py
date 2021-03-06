# Generated by Django 3.2.8 on 2022-03-23 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=50)),
                ('departament', models.CharField(max_length=50)),
                ('town', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Specie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kingdom', models.CharField(max_length=50)),
                ('edge', models.CharField(max_length=50)),
                ('classe', models.CharField(max_length=50)),
                ('family', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=20)),
                ('specie', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sighting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scientific_name', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('latitude', models.CharField(max_length=30)),
                ('longitude', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=50)),
                ('grades', models.CharField(max_length=50)),
                ('specie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invemar.specie')),
            ],
        ),
    ]
