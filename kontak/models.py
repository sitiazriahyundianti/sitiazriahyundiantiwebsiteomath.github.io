from django.db import models

# Create your models here.

class Tanggal(models.Model):
    tanggal = models.IntegerField

class Bulan(models.Model):
    bulan = models.IntegerField

class Tahun(models.Model):
    tahun = models.IntegerField

class Provinsi(models.Model):
    nama_provinsi = models.CharField(max_length=20)

class Kota(models.Model):
    nama_kota = models.CharField(max_length=20)

class About(models.Model):
    nama = models.CharField(max_length=80)
    tanggal_lahir = models.DateField(max_length=50)
    alamat_rumah = models.TextField(max_length=200)
    hobi = models.CharField(max_length=80)
    nomor_telepon = models.IntegerField
    email = models.CharField(max_length=80)
    instagram = models.CharField(max_length=80)
    tanggal_id = models.ForeignKey(Tanggal, on_delete=models.CASCADE, null=True)
    bulan_id = models.ForeignKey(Bulan, on_delete=models.CASCADE, null=True)
    tahun_id = models.ForeignKey(Tahun, on_delete=models.CASCADE, null=True)
    provinsi_id = models.ForeignKey(Provinsi, on_delete=models.CASCADE, null=True)
    kota_id = models.ForeignKey(Kota, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.nama