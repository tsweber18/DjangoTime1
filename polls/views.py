from django.shortcuts import render
from django.http import HttpResponse
import time
# Create your views here.

def index(request):
    return HttpResponse("Hello World.  This is Django, and it is " + time.strftime("%c"))