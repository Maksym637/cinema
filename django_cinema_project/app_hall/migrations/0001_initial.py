# Generated by Django 3.2.15 on 2022-10-05 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_seat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_people', models.IntegerField()),
                ('number', models.IntegerField()),
                ('seat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_seat.seat')),
            ],
            options={
                'verbose_name': 'Зал',
                'verbose_name_plural': 'Залы',
                'db_table': 'halls',
            },
        ),
    ]
