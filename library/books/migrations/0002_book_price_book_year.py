# Generated by Django 4.2.11 on 2024-03-28 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='year',
            field=models.DateField(null=True),
        ),
    ]
