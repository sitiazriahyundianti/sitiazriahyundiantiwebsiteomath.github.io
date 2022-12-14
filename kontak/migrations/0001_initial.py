# Generated by Django 4.1.1 on 2022-10-16 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bulan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Kota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_kota', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Provinsi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_provinsi', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tahun',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Tanggal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=80)),
                ('tanggal_lahir', models.DateField(max_length=50)),
                ('alamat_rumah', models.TextField(max_length=200)),
                ('hobi', models.CharField(max_length=80)),
                ('email', models.CharField(max_length=80)),
                ('instagram', models.CharField(max_length=80)),
                ('bulan_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kontak.bulan')),
                ('kota_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kontak.kota')),
                ('provinsi_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kontak.provinsi')),
                ('tahun_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kontak.tahun')),
                ('tanggal_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kontak.tanggal')),
            ],
        ),
    ]
