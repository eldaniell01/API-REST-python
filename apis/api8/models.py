from django.db import models

# Create your models here.

class Proveedor(models.Model):
    name = models.CharField(max_length=150)
    def __str__(self):
        return f'{self.name}'
    
    
class Moto(models.Model):
    name = models.CharField(max_length=150)
    modelo = models.IntegerField()
    marca = models.CharField(max_length=150)
    def __str__(self):
        return f'{self.name}'

class Repuesto(models.Model):
    code = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.IntegerField()
    state = models.BooleanField(default=False)
    image = models.ImageField(upload_to='repuestos', blank=True, null=True)
    id_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    id_moto=models.ForeignKey(Moto, on_delete=models.CASCADE)
    
    class Meta: 
        ordering=('name',)
    def __str__(self):
        return f'{self.name}'