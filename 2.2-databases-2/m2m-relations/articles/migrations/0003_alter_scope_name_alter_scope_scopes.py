# Generated by Django 4.0.6 on 2022-08-16 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_relationship_scope_relationship_scope'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scope',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='scope',
            name='scopes',
            field=models.ManyToManyField(related_name='scopes', through='articles.Relationship', to='articles.article'),
        ),
    ]
