
from django.contrib import admin
from django.urls import path

from webapp.views import bienvenido, despedirse

urlpatterns = [
    path("admin/", admin.site.urls),
    #path("/", bienvenido)
    path("", bienvenido),
    path('despedida.html', despedirse)
]

