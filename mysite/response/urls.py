from django.urls import path
from . import views

#response urls
urlpatterns = [
    path('info/', views.more_info, name='more_info'),
]
