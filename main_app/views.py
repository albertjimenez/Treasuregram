from django.shortcuts import render
from django.db import models


# Create your views here.
def index(request: "django_request"):
    listaTesoros = [Treasure('Gold Nugget', 500.00, 'gold', "Curly's Creek, NM"),
                    Treasure("Fool's Gold", 0, 'pyrite', "Fool's Falls, CO"),
                    Treasure('Coffee Can', 20.00, 'tin', 'Acme, CA')]
    context = {'treasures': listaTesoros}
    return render(request, 'index.html', context)


# My Treasure class
class Treasure(models.Model):
    # OldFashioned way
    # def __init__(self, name: "String", value: "Int", material: "String", location: "Int"):
    #     self.name = name
    #     self.value = value
    #     self.material = material
    #     self.location = location
    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    material = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    img_url = models.CharField(max_length=100)
