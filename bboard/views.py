from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Bb


def index(request):
    template = loader.get_template('index.html')
    bbs = Bb.objects.order_by('-published')
    context = {'bbs': bbs}
    return HttpResponse(template.render(context, request))