from django.http import Http404
from django.shortcuts import render
from .models import Visit


def visit_list(request):
    context = {}
    context["TITLE"]="EasyLab"
    context["visitlist"]=Visit.objects.all()

    return render(request, 'receipts/visitlist.html', context)
