from django.db import models

# Create your models here.
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

    def __str__(self):
        return self.name