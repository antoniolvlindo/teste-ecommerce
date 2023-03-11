from django.http import HttpResponse
from django.shortcuts import render


def register(request):
    return HttpResponse('Account url setup!')
