from ctypes.wintypes import WORD
from django.shortcuts import render
from django.http import HttpResponse
from . import sinhala_converter as conv
from . import database_handler as db_handler
# Create your views here.

def app(request) :
    return render(request, "index.html")

def convert_sentence(converter, sentence) :
    split_sent = sentence.split(" ")
    res = []

    for x in split_sent :
        res.append(converter.convert_to_sinhala(x))

    return " ".join(res)

def call(request) :
    sentence = request.POST['english']
    sin_conv = conv.SinhalaConverter()
    result = convert_sentence(sin_conv,sentence)
    print(sentence)
    connn = {
        "conv_sent":result,
        "org_txt":sentence
    }
    return render(request, "index.html", connn)

    