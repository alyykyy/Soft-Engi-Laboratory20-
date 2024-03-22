from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Hello World")

def myfirst(request):
    return render(request, 'myfirst.html')

"""
def sdc_view(request):
    return render(request, 'sdcFile.html')
"""

def sdc_file_view(request):
    return render(request, 'sdcFile.html')



