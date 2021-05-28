from django.shortcuts import render

from django.http import HttpResponse
items=[
        {'phone':'Redmi 6a',
         'screen':'6inch',
          'price':'7000'},

        {'phone':'Realme 6',
         'screen':'8inch',
         'price':'12000'},

        {'phone':'poco x3', 
        'screen':'9inch', 
        'price':'18000'},
    ]
 
def index(request):
    context = {
        'items':items
    }
    return render(request, 'report/home.html', context)  # \ plz put template path inside the single quote & don't do spell mistake
    
def base_view(request):
    return render(request, 'report/base.html')





#user request for httpRequest// system answer with httpResponse 