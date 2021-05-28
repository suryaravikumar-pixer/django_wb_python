from django.urls import path
from . import views

#app urls
urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.base_view, name='base'),
]
