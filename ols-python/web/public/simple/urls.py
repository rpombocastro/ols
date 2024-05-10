"""
URL configuration for simple project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.views.static import serve
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

@login_required(login_url='/not-found/', redirect_field_name=None)
def protected_serve(request, path, document_root=None, show_indexes=False):
    return serve(request, path, document_root, show_indexes)

def IndexView(request):
    return render(request, "index.html")

urlpatterns = [

    path('', IndexView),
    # SE CAMBIA LA DIRECCIÓN POR DEFECTO POR SEGURIDAD
    # NOTA: Activar si se trabaja con base de datos
    # path('4m1str4d0r/', admin.site.urls),

    # URLS DE LOS MÓDULOS
    # path('', include('apps.<dirección del archivo url del módulo>')),

    # SI UTILIZAMOS LOS ARCHIVOS ESTATICOS Y MEDIA EN LOCAL DEBEMOS ACTIVAR ESTA PARTE
    # URL DE LOS STATIC FILES CUANDO DEBUG = False
    # EN deploy.py STATIC_URL='staticfiles'
    # re_path(r'^%s(?P<path>.*)$' % settings.STATIC_URL[1:], serve,{'document_root': settings.STATIC_ROOT}),

    # URL for block media files (ESTO NO ES NECESARIO)
    # re_path(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], protected_serve, {'document_root': settings.MEDIA_ROOT}),
    
    re_path(r'^favicon\.ico$',  RedirectView.as_view(url=staticfiles_storage.url('img/logos/favicon.ico'), permanent=True)),
]
