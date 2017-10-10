from django.http import Http404, HttpResponse
# from django.shortcuts import render
from .models import Visit

from django.template import loader


def visit_list(request):
    context = {}
    context["TITLE"]="EasyLab"
    context["visitlist"]=Visit.objects.all()
    template = loader.get_template('receipts/visitlist.html')
    return HttpResponse(template.render(context, request))

def follow_up(request):
    context = {}
    context["TITLE"]="EasyLab"
    context["visitlist"] = Visit.objects.filter(status="Not Completed")
    template = loader.get_template('receipts/followup.html')
    return HttpResponse(template.render(context, request))
def completed(request):
    context = {}
    context["TITLE"]="EasyLab"
    context["visitlist"] = Visit.objects.filter(status="Completed")
    template = loader.get_template('receipts/completed.html')
    return HttpResponse(template.render(context, request))
