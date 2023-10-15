from django.shortcuts import render
from django.http import JashResponse
# Create your views here.

def getRoutes(request):
    return JashResponse('helo', safe=False)

