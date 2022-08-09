# Generated by Django 4.0.6 on 2022-08-09 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('price', models.ImageField(max_length=50, upload_to='')),
                ('image', models.ImageField(max_length=50, upload_to='')),
                ('release_date', models.CharField(max_length=50)),
                ('lte_exists', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
            ],
        ),
    ]
