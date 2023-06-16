from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField
from django import forms

# Create your models here.


# la clase models nos ayudara a definir que queremos guardar dentro del proyecto.
class Project(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=250)
    # debemos indicar donde se ubicaran las imagenes
    image = ImageField(upload_to='portfolio/images')
    url = URLField(blank=True)

