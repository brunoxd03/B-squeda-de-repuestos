from django.shortcuts import render
from django.http  import HttpResponse
from .models import Project, Task,Ventiladores
from django.db.models import Q

# Create your views here.

def index(request) : 
    title = 'Bienvenidos al buscador de partes/repuestos de Ventituc'
    #index_form = IndexForm()
    return render(request,'index.html')


def projects(request):
    busqueda = request.GET.get("buscar")
    modelos = Project.objects.all()
    
    if busqueda:
        modelos = Project.objects.filter(
        Q(name__icontains = busqueda) | 
        Q(description__icontains = busqueda)
    ).distinct()
    return render(request, 'projects/projects.html', {'modelos': modelos})

def task(request):
    tasks = Task.objects.all()
    busqueda_2 = request.GET.get("buscar")
    if busqueda_2:
        tasks = Task.objects.filter(
            Q(title__icontains = busqueda_2) |
            Q(description__icontains = busqueda_2) |
            Q(modelo_vt__icontains = busqueda_2)
        ).distinct()
    return render(request, 'task/task.html',{
        'tasks':tasks,
        })
          
def ventilador_search(request):
    resultados_vt = Ventiladores.objects.all()
    busqueda_3 = request.GET.get("buscar")
    if busqueda_3:
        resultados_vt = Ventiladores.objects.filter(
            Q(nombre__icontains=busqueda_3) | 
            Q(descripcion__icontains=busqueda_3)
        ).distinct()
    return render(request, 'search_ventilador.html', {'resultados_vt': resultados_vt})

def ver_repuestos(request, nombre_ventilador): #Filtrar repuesto por el nombre del ventilador
    repuestos = Task.objects.filter(modelo_vt__iexact=nombre_ventilador)
    return render(request, 'task/task.html', {'tasks': repuestos, 'nombre_ventilador': nombre_ventilador})


def ver_despiece(request, nombre_ventilador):  #Filtrar despiece por el nombre del ventilador
    despiece = Ventiladores.objects.filter(nombre__iexact=nombre_ventilador)
    return render(request, 'search_ventilador.html', {'resultados_vt': despiece, 'query': nombre_ventilador})