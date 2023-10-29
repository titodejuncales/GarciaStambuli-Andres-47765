from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Moneda(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    pais = models.CharField(max_length=20)
    continente = models.CharField(max_length=20, blank=True, null=True)
    valor = models.CharField(max_length=20)  
    year = models.IntegerField()
    material = models.CharField(max_length=30)
    forma = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    imgfrente = models.ImageField(upload_to='monedas', blank=True, null=True)
    imgdorso = models.ImageField(upload_to='monedas', blank=True, null=True)

    def __str__(self):
        return f"Moneda de {self.pais} del año {self.year} de {self.valor}" 
    
    class Meta:
        verbose_name = "Moneda"
        verbose_name_plural = "Monedas"
    
class Billete(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    pais = models.CharField(max_length=20)
    continente = models.CharField(max_length=20, blank=True, null=True)
    valor = models.CharField(max_length=20)  
    year = models.IntegerField()
    material = models.CharField(max_length=30, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    imgfrente = models.ImageField(upload_to='billetes', blank=True, null=True)
    imgdorso = models.ImageField(upload_to='billetes', blank=True, null=True)
   
    def __str__(self):
        return f"Billete de {self.pais} del año {self.year} de {self.valor}" 
    
    class Meta:
        verbose_name = "Billete"
        verbose_name_plural = "Billetes"
    
class Estampilla(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    pais = models.CharField(max_length=20)
    valor = models.CharField(max_length=20)  
    year = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    forma = models.CharField(max_length=20, blank=True, null=True)
    imgfrente = models.ImageField(upload_to='estampillas', blank=True, null=True)
      
    def __str__(self):
        return f"Estampilla de {self.pais} de {self.valor}" 
    
    class Meta:
        verbose_name = "Estampilla"
        verbose_name_plural = "Estampillas"

class FichayMedalla(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipodeobjeto = models.CharField(max_length=20)
    pais = models.CharField(max_length=20, blank=True, null=True)
    valor = models.CharField(max_length=20, blank=True, null=True)  
    year = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    forma = models.CharField(max_length=20, blank=True, null=True)
    imgfrente = models.ImageField(upload_to='fichasymedallas', blank=True, null=True)
    imgdorso = models.ImageField(upload_to='fichasymedallas', blank=True, null=True)
      
    def __str__(self):
        return f"{self.tipodeobjeto} de {self.pais}" 
    
    class Meta:
        verbose_name = "Ficha/Medalla"
        verbose_name_plural = "Fichas/Medallas"
    

