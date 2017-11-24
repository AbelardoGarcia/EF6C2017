# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required 
from django.core.urlresolvers import reverse 
from django.shortcuts import render_to_response, render, redirect 
from django.template import RequestContext 
from django.conf import settings 
from django.http import HttpResponseRedirect, HttpResponse 
from django.contrib.auth import login, logout, authenticate 
from django.contrib.auth.models import AnonymousUser 
from django.contrib import messages 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 
from django.db.models import Q 
from datetime import datetime, timedelta 
from django.utils import timezone
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

# Create your views here.
from votos.models import *


def resultado_global(request):
    """
    Generar la vista para devolver el resultado global de la elección.
    Tener en cuenta que tiene que tener:
    Cantidad total de votos por candidato
    Cantidad total de votos nulos
    Porcentaje de cada candidato
    Porcentaje de votos nulos
    Total de votos de la elección
    """
    
    context={}
    context['distritos'] = Distrito.objects.all()
    #TODO TU CODIGO AQUI

    return render(request,'global.html',context)


def resultado_distrital(request):
    """
    Generar la vista para devolver el resultado distrital de la elección
    Tener en cuenta que tiene que tener:
    Tamaño del padrón
    Porcentaje de votos del distrito (respecto al padron. Ejemplo: Si el distrito tiene 1000 votantes y hay 750 votos, el porcentaje es 75%)
    Total de votos del distrito
    Candidato ganador
    """
    context={}

    #TODO TU CODIGO AQUI

    return render(request,'distrital.html',context)
