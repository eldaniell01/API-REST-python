from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'moto', views.MotoViewSet)
router.register(r'proveedor', views.ProveedorViewSet)
router.register(r'repuesto', views.RepuestoViewSet)
urlpatterns = [
    path('', include(router.urls))
]
