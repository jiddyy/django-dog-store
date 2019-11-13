"""dog_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
import app.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", app.views.home, name="home"),
    path("dog-product/<dog_product_id>", app.views.dog_product_detail, name="dog_product_detail"),
    path("dog-product/<dog_product_id>/purchase", app.views.purchase_dog_product, name="purchase_dog_product"),
    path("purchase/<purchase_id>", app.views.purchase_detail, name="purchase_detail"),
    path("dogtag/new", app.views.new_dog_tag, name="new_dog_tag"),
    path("dogtag", app.views.dog_tag_list, name="dog_tag_list")
]
