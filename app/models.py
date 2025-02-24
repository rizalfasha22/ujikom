from django.db import models

# Create your models here.
class Product(models.Model):
    CATEGORY = (
        ("sepatu", "Sepatu"),
        ("baju", "Baju"),
        ("jaket", "Jaket")
    )

    gambar = models.ImageField(upload_to="image/")
    nama = models.CharField(max_length=255, null=False, blank=False)
    harga = models.DecimalField(max_digits=25, decimal_places=0)
    stok = models.IntegerField()
    kategori = models.CharField(max_length=255, choices=CATEGORY)
    deskripsi = models.TextField(null=False)