# Generated by Django 3.2.16 on 2022-10-14 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=50)),
                ('language', models.CharField(max_length=50)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('year', models.DateTimeField()),
                ('rate', models.IntegerField()),
            ],
            options={
                'db_table': 'films',
                'ordering': ['year'],
            },
        ),
    ]
