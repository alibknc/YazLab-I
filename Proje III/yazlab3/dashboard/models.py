from django.db import models
from django.contrib.auth.models import User

class File(models.Model):
    yazarAdi = models.CharField(max_length=100, null=True)
    numara = models.CharField(max_length=100, null=True)
    dersAdi = models.CharField(max_length=100, null=True)
    juriler = models.CharField(max_length=100, null=True)
    donem = models.CharField(max_length=100, null=True)
    ozet = models.CharField(max_length=2500, null=True)
    danisman = models.CharField(max_length=100, null=True)
    anahtarKelimeler = models.CharField(max_length=100, null=True)
    baslik = models.CharField(max_length=100, null=True)
    ogretim = models.CharField(max_length=100, null=True)
    pdf = models.FileField(upload_to='files/pdfs/', null=True)
    hocaID = models.IntegerField(null=True)

    def __str__(self):
        return self.numara

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs)

