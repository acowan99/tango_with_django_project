from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hi" + '<br/>' + '<a href="/rango/about/">About</a>')

def about(request):
    return HttpResponse("ABOUT PAGE" + '<br/>' + '<a href="/rango/">INDEX</a>')

