# Generated by Django 4.1.1 on 2022-10-16 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mahasiswa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('materi', models.CharField(max_length=80)),
                ('soal', models.TextField(max_length=200)),
                ('kunci_jawaban', models.TextField(max_length=200)),
            ],
        ),
    ]
