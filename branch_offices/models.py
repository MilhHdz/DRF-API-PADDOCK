from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

# Create your models here.
class Sucursal(TenantMixin):
    nombre = models.CharField(max_length=100)
    creado = models.DateField(auto_now_add=True)

    auto_create_schema = True

    class Meta:
        db_table = "sucursal"


class Domain(DomainMixin):
    
    class Meta:
        db_table = "dominio"