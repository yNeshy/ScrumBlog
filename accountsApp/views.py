from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Users

def home(request):
    num_visits = request.session.get('num_visits', 0)
    
    if request.method == 'POST' :
        return do_post(request)

    else :
        if request.method == 'GET' :
            return do_get(request)
        else :
            return HttpResponse("404 not found error please contact administrator")


def do_get(request):
    return render( request,
                   'accountsApp/login.html' , {'redirected': False} )
 
def do_post(request):
    username = request.POST.get('login', '')
    password = request.POST.get('pass', '')

    
    result =  Users.objects.filter(username=username, password=password)
    
    if not result :
        return render(request,
                      'accountsApp/login.html',{'redirected': True} )
    else :
        return redirect('articlesApp:main')
    
