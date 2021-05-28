from django.shortcuts import render
from . import views
# Create your views here.
def more_info(request):
    return render(request, 'response/more_info.html')