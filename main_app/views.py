from django.shortcuts import render
from .models import Treasure

# Create your views here.
def index(request: "django_request"):
    treasure = Treasure.objects.all()
    context = {'treasures': treasure}
    return render(request, 'index.html', context)


# My Treasure class
