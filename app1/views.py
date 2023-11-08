from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ram(request):
    return HttpResponse('<h1><marquee><bgcolor:orange>|| JAI SHREE RAM ||</h1></marquee>')
def mohan(request):
    return HttpResponse('<h1><marquee>|*| JAI SHREE RAM || JAI SHREE RAM |*|</h1></marquee>')