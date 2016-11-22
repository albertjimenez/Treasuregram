from django.shortcuts import render

# Create your views here.
def index(request :"django_request"):
    return render(request,'index.html')