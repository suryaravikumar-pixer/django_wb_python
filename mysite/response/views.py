from django.shortcuts import render

# Create your views here.


def more_info(request):
    return render(request, 'response/more_info.html')