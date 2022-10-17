from django.db import models

# Create your models here.

class Nama_Materi(models.Model) :
    nama_materi = models.CharField(max_length=80)

class Soal(models.Model):
    materi = models.CharField(max_length=80)
    soal = models.TextField(max_length=200)
    kunci_jawaban = models.TextField(max_length=200)
    nama_materi_id = models.ForeignKey(Nama_Materi, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.materi