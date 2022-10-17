# Generated by Django 4.1.1 on 2022-10-17 19:43


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_film', '0001_initial'),
        ('app_hall', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_start', models.TimeField()),
                ('time_end', models.TimeField()),
                ('date', models.DateField()),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_film.film')),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_hall.hall')),
            ],
            options={
                'db_table': 'schedules',
                'ordering': ['date'],
            },
        ),
    ]
