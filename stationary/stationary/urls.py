"""stationary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from stationary.views import *

"""
from stationary.views import index
from stationary.views import products
from stationary.views import products_case
from stationary.views import products_note
from stationary.views import products_pen
from stationary.views import products_pencil
"""


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('products', products, name='products'),
    path('products_case', case, name='products_case'),
    path('products_note', note, name='products_note'),
    path('products_pen', pen, name='products_pen'),
    path('products_pencil', pencil, name='products_pencil'),
]
