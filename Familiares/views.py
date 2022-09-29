# from re import template
# from unittest import loader
from django.shortcuts import render, HttpResponse
from django.template import loader, Template

from Familiares.models import Persona


def familia(request):
    template = loader.get_template("familia.html")

    familiar_1 = Persona(
        nombre="Arnold",
        apellido="Schwarzenegger",
        fecha_de_nacimiento="1947-07-30",
        edad=75,
    )
    familiar_2 = Persona(
        nombre="Maria",
        apellido="Shriver",
        fecha_de_nacimiento="1955-11-06",
        edad=66
    )
    familiar_3 = Persona(
        nombre="Katherine",
        apellido="Schwarzenegger",
        fecha_de_nacimiento="1989-12-13",
        edad=32,
    )
    familiar_4 = Persona(
        nombre="Patrick",
        apellido="Schwarzenegger",
        fecha_de_nacimiento="1993-08-19",
        edad=29,
    )
    familiar_1.save()
    familiar_2.save()
    familiar_3.save()
    familiar_4.save()
    ctx = {
        "familiar_1": familiar_1,
        "familiar_2": familiar_2,
        "familiar_3": familiar_3,
        "familiar_4": familiar_4,
    }

    fam = template.render(ctx)
    return HttpResponse(fam)