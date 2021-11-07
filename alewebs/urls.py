from django.urls import path

from . import views

app_name = 'alewebs'

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('price/', views.price, name="price"),
    path('features/', views.features, name="features")
]
