from django.contrib import admin
from django.urls import path, include
from branch_offices.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registro/', include(router.urls)),
]