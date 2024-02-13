from django.shortcuts import render

from platform_student.models import Section, Material
from django.views.generic import ListView, DetailView


def index(request):
    section_list = Section.objects.all()
    context = {
        'section_list': section_list
    }
    return render(request, "platform_student/base.html", context)


def material_list(request, section_id):
    section = Section.objects.get(pk=section_id)
    materials = Material.objects.filter(section=section)
    return render(request, 'platform_student/material_list.html', {'section': section, 'materials': materials})


class MaterialDetailView(DetailView):
    model = Material
