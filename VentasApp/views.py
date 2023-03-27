from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import *
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
#from django.http import HttpResponse
#from django.template import loader
# Create your views here.

def login(request):
    return render (request,'Inicio.html')

def register(request):
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'usuario {username} creado')
            return redirect('login')
    else:
        form = UserRegisterForm()

    context = { 'form' : form }
    return render(request, 'registration/registro.html', context)

def cerrarSesion(request):
    logout(request)
    return redirect('/')

@login_required
def inicio(request):
    item_list = Item.objects.all()
    context = {
        'item_list' : item_list
    }
    return render(request,'Inicio.html',context)

@login_required
def add_item(request):
    if request.method=="POST":
        name = request.POST['name']
        description = request.POST['description']
        item = Item(name = name,description = description)
        item.save()
        messages.info(request,"se agrego correctamente")
        return redirect(inicio)
    else:
        pass

    form = Item.objects.all()
    context = {
        'forms' : form
    }
    return render(request,'Inicio.html',context)

def delete_item(request,myid):
    item = Item.objects.get(id= myid )
    item.delete()
    messages.info(request,"se elimino correctamente")
    return redirect(inicio)
    
def listadoproducto(request):
    form = Item.objects.all()
    return render (request,'Inicio.html',{ 'forms' : form })