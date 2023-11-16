from ctypes.wintypes import WORD
from django.shortcuts import render
from django.http import HttpResponse
from . import sinhala_converter as conv
from . import database_handler as db_handler
from django.urls import path
# Create your views here.

def app1(request) :
    return render(request, "index.html")

def convert_sentence(converter, sentence) :
    split_sent = sentence.split(" ")
    res = []

    for x in split_sent :
        res.append(converter.convert_to_sinhala(x))

    return " ".join(res)

def call(request) :
    import urls as url
    url.urlpatterns2.append(path('app/app1', app1, name="app1"))



    