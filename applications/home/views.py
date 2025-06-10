from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView

from django.contrib.auth import login, logout, authenticate

import json

with open("secrets.json") as s:
    secrets = json.load(s)

class IndexView(TemplateView) :
    template_name = 'home/index.html'


def sessionLogIn(request):
    if request.method == "GET":
        return render(request, 'login/login.html')
    elif request.method == "POST":
        if not request.POST['username'] and not request.POST['password'] :
            return render(request, 'login/login.html',{
                    "error": 'No se han completado todos los datos.'
                })
        else :
            user = authenticate(request, username = request.POST['username'] , password = request.POST['password'])
            if user is None :
                return render(request, 'login/login.html',{
                    "error": 'Los datos ingresados son incorrectos.'
                })
            else:
                login(request, user)
                return redirect(secrets["HOME_URL"] or 'http://127.0.0.1:8000/')


def sessionLogOut(request) :
    logout(request)
    return redirect(secrets["HOME_URL"] or 'http://127.0.0.1:8000/')