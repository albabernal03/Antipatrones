from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('CalculadoraApp/', include('CalculadoraApp.urls')),
    path('', include('CalculadoraApp.urls')),  # Add this line for the root path
]
