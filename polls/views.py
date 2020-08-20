from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    return HttpResponse("Você esta visualizando a questão %s" % question_id)

def results(request, question_id):
    response = "Você esta visualizando os resultados da questão %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Você esta votando na questão %s" % question_id)
    