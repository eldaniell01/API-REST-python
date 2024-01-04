from django.contrib import admin
from .models import Proveedor, Moto, Repuesto
# Register your models here.

admin.site.register(Moto)
admin.site.register(Proveedor)
admin.site.register(Repuesto)
