from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader
import random

from home.models import Familiar

def hola_mundo(request):
    
    template = loader.get_template('hola.html')
    template_renderizado = template.render()
    
    return HttpResponse(template_renderizado)

def crear_familiar(request):    
    familiar1 = Familiar(nombre='Eduardo', apellido='Deluca', fe_nacimiento = datetime(1922,2,4), edad=100, descPariente='Padre')
    familiar2 = Familiar(nombre='Rosa', apellido='Nuñez', fe_nacimiento = datetime(1924,2,3), edad=98, descPariente='Madre')
    familiar3 = Familiar(nombre='María Cristina', apellido='Deluca', fe_nacimiento = datetime(1950,4,7), edad=72, descPariente='Hermana')
    familiar4 = Familiar(nombre='Graciela', apellido='Deluca', fe_nacimiento = datetime(1952,4,7), edad=70, descPariente='Hermana')
    familiar1.save()
    familiar2.save()
    familiar3.save()
    familiar4.save()
    template = loader.get_template('crear_familiar.html')
    template_renderizado = template.render({})
    return HttpResponse(template_renderizado)

def ver_familiares(request):
    
    familiares = Familiar.objects.all()
    
    template = loader.get_template('ver_familiares.html')
    template_renderizado = template.render({'familiares':familiares})
    
    return HttpResponse(template_renderizado)