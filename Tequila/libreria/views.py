from django.shortcuts import render,  redirect
from django.http import HttpResponse
from libreria import templates
from django.contrib import messages
from django.contrib.auth import authenticate, login


# Create your views here.

def inicio(request):
     return render(request, 'inicio.html')
def login(request):
     return render(request, 'login.html')     


def registro(request):
     data = {
          'form': registro
     }

     if request.method == 'POST':
          formulario = registro(data=request.POST)
          if formulario.is_valid():
               formulario.save()
               user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password"])
               login(request, user)
               messages.success(request,"Te has registrado correctamente" )
               return redirect (to= "inicio.html")
          data["form"] = formulario    


     return render(request, 'registro.html', data)