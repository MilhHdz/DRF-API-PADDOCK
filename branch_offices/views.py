from .models import Sucursal, Domain
from .serializers import DomainSerializer
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

# Create your views here.
class SucursalCreateView(viewsets.GenericViewSet,mixins.CreateModelMixin):
    serializer_class = DomainSerializer

    def create(self, request):
        """
            Permiteque se cree una nueva sucursal
        """
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            schema = self.nombrar_schema(request.data['domain'])
            sucursal = Sucursal(schema_name=schema, nombre=request.data['tenant']['nombre'])
            sucursal.save()

            dominio = Domain()
            dominio.domain = request.data['domain']
            dominio.tenant = sucursal
            dominio.is_primary = request.data['is_primary']
            dominio.save()

            return Response(serializer.data, status=HTTP_201_CREATED)

        return Response(
            {"detail": "error", "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

    
    def nombrar_schema(self, dominio):
        nombre = '_'.join(dominio.split('.')[::-1])
        return nombre