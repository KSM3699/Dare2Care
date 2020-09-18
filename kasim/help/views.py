from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def kasimsheikh(request):
    return render(request,'kasimsheikh.html')