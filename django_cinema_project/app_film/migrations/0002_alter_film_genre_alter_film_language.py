# Generated by Django 4.1.1 on 2022-10-18 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_film', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='genre',
            field=models.CharField(choices=[('Comedy', 'Comedy'), ('Crime', 'Crime'), ('Drama', 'Drama'), ('Fantasy', 'Fantasy'), ('Horror', 'Horror')], default='Comedy', max_length=20),
        ),
        migrations.AlterField(
            model_name='film',
            name='language',
            field=models.CharField(choices=[('English', 'English'), ('Spanish', 'Spanish'), ('French', 'French'), ('Ukrainian', 'Ukrainian')], default='English', max_length=20),
        ),
    ]
