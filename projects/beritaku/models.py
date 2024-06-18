from django.db import models
import os
from uuid import uuid4

# Create your models here.
class Data_Berita(models.Model):
    id = models.AutoField(primary_key=True)
    judul = models.CharField(max_length=50, blank=True, null=True)
    berita = models.TextField(blank=True, null=True)
    gambar = models.ImageField(upload_to='img/')
    kategori = models.CharField(max_length=15, blank=True, null=True)
    id_user = models.CharField(max_length=15, blank=True, null=True)
    tanggal = models.DateField(blank=True, null=True)
    
    class Meta:
     db_table = 'dt_berita'


class Data_Pengguna(models.Model):
    id = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    tanggal = models.DateField(blank=True, null=True)

    class Meta:
     db_table ='user_account'