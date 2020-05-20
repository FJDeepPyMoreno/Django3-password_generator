"""password_generator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
#from django.contrib import admin
from django.urls import path
##
from generator import views
##
from django.views.generic import RedirectView
from django.conf.urls import url


#urlpatterns = [
#    path('admin/', admin.site.urls),
#]

urlpatterns = [path('', views.home,name = 'home'),
        path('generatedpassword/', views.password, name = 'password'),
        path('aboutme/', views.about, name = 'about'),
        url(r'^favicon\.ico$',
            RedirectView.as_view(url='/static/images/favicon.ico'))]
## urlpatterns contiene los matching paths de nuestro website, ejemplo:
## localhost:8000/admin mos lleva a una página válida. Mientras que si
## pongo: localhost:8000/holaPepe, se lanza un error 404, ya que
## 'holaPepe' no está defnida en path.


