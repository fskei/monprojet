# Generated by Django 5.2.4 on 2025-07-03 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Capteur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('date_installation', models.DateField()),
                ('actif', models.BooleanField(default=True)),
            ],
        ),
    ]
