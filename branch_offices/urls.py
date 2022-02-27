from rest_framework.routers import DefaultRouter
from .views import SucursalCreateView

router = DefaultRouter()

router.register(r'sucursal',SucursalCreateView, basename='Registro de Sucursal')