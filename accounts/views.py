from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_POST
from .models import perfil


from django.urls import reverse_lazy

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        name = request.POST.get('name')
        password = request.POST.get('password')

        user = authenticate(request, name = name, password = password)

        if user.is_active:
            login(request, user)
    
       

def logout(request):
    logout(request)



def cadastrar_usuario(request):

    if request.method == 'POST':
        nome_usuario = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        newUser = User.objects.create(username = nome_usuario, email = email, password = password)
        newUser.save()

        return redirect('login')

    template = loader.get_template('registration/register.html')
    return HttpResponse(template.render({}, request))

 


    


