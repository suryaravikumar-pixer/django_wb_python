from django.urls import path
from . import views as pooja

#response urls
urlpatterns = [
    path('info/', pooja.more_info, name='more_info'),
]
