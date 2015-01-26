from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.template import RequestContext, loader

#import models from www if there are any

def index(request):
    return render(request, 'site_flow/index.html')

def about(request):
    return render(request, 'site_flow/about.html')

def faq(request):
    return render(request, 'site_flow/faq.html')
