"""
URL configuration for empleados project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from applications.home.views import IndexView, sessionLogIn, sessionLogOut
from applications.departamentos.views import ListarDepartamentos
from applications.empleados.views import EmpleadoListView, EmpleadoDetailView, EmpleadoCreateView, EmpleadoUpdateView, EmpleadoDeleteView
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/home/', permanent=False)),
    path('home/', IndexView.as_view(), name='home'),
    path('sign-in/', sessionLogIn, name='login'),
    path('log-out/', sessionLogOut, name='logout'),
    path('lista-departamentos', ListarDepartamentos.as_view(), name='departamentos'),
    path('empleados/', EmpleadoListView.as_view(), name='empleado_list'),
    path('empleados/empleado/<int:pk>/', EmpleadoDetailView.as_view(), name='empleado_detail'),
    path('empleados/crear/', EmpleadoCreateView.as_view(), name='empleado_create'),
    path('empleados/empleado/<int:pk>/editar/', EmpleadoUpdateView.as_view(), name='empleado_update'),
    path('empleados/empleado/<int:pk>/eliminar/', EmpleadoDeleteView.as_view(), name='empleado_delete'),
    
    #CKEDITOR
    path('ckeditor5/', include('django_ckeditor_5.urls')),
]
