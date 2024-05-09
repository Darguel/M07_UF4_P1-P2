from unittest import loader
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .forms import UsuariForm
from django.shortcuts import redirect
from . import models

# Create your views here.

def home(request):
    return HttpResponse("Hello, wolrd")

def about(request):
    return HttpResponse("<h1>About</h1>")

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def students(request):
    student = [
        {"id":1,"nom":"David","cognom1":"Argüelles","cognom2":"López","correu":"david@gmail.com","curs":"DAW2A","moduls":"MO7"},
        {"id":2,"nom":"Joan","cognom1":"Martinez","cognom2":"Ros","correu":"joan@gmail.com","curs":"DAW2B","moduls":"MO8"},
        {"id":3,"nom":"Maria","cognom1":"Bas","cognom2":"Silva","correu":"maria@gmail.com","curs":"DAM2A","moduls":"MO9"}
    ]

    template = loader.get_template('students.html')
    return render(request, 'students.html', {'students': student})

def teacher(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def user_form(request):
    form = UsuariForm()

    if request.method == 'POST':
        form = UsuariForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showAll')

    context = {'form': form}
    return render(request, 'form.html', context)

def show_all(request):
    usuari= list(models.Usuari.objects.all())
    
    return render(request,'formInfo.html',{'usuaris': usuari})

def user_update(request, id):
    usuari = models.Usuari.objects.get(id=id)
    form = UsuariForm(instance=usuari)

    if request.method == 'POST':
        form = UsuariForm(request.POST, instance=usuari)
        if form.is_valid():
            form.save()
            return redirect('showAll')

    context = {'form': form, 'user': usuari}
    return render(request, 'formUpdate.html', context)

def user_delete(request, id):
    usuari = models.Usuari.objects.get(id=id)
    
    if request.method == 'POST':
        usuari.delete()
        return redirect('showAll')

    context = {'user': usuari}
    return render(request, 'formDelete.html', context)
