# Generated by Django 3.1.4 on 2020-12-19 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=200)),
                ('suite', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('zipcode', models.CharField(max_length=200)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('catchPhrase', models.CharField(max_length=500)),
                ('bs', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('username', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=30)),
                ('website', models.CharField(max_length=300)),
                ('address', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='groupapp.address')),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='groupapp.company')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('body', models.TextField()),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groupapp.user')),
            ],
        ),
    ]
