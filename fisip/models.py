from django.db import models

# Create your models here.

class Mahasiswa(models.Model):
    NIM = models.IntegerField(null=True)
    nama = models.CharField(max_length=50)
    tanggal_lahir = models.DateField(max_length=50)
    photo = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    fakultas = models.CharField(max_length=50)
    prodi = models.CharField(max_length=50)

    def __str__(self):
        return self.nama

class Tendik(models.Model):
    NIP = models.IntegerField(null=True)
    nama = models.CharField(max_length=50)
    tanggal_lahir = models.DateField(max_length=50)
    photo = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    unit = models.CharField(max_length=50)
    alamat_rumah = models.CharField(max_length=50)

    def __str__(self):
        return self.nama

class Dosen(models.Model):
    NIP = models.IntegerField(null=True)
    nama = models.CharField(max_length=50, null=True)
    tanggal_lahir = models.DateField(max_length=50, null=True)
    photo = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    fakultas = models.CharField(max_length=50, null=True)
    prodi = models.CharField(max_length=50, null=True)
    alamat_rumah = models.CharField(max_length=60, null=True)
    tendik_id = models.ForeignKey(Tendik, on_delete=models.CASCADE, null=True)
    mahasiswa_id = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nama