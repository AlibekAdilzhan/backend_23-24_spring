from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def books(request):
    return HttpResponse("Hello world")