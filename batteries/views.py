from django.shortcuts import render
from batteries.models import *
from django.views.generic import ListView, DetailView, TemplateView
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404
#from django.core.context_processors import csrf
#from django.views.decorators.csrf import csrf_exempt
#from datetime import *
#import random
#import string

# Create your views here.
def index(request):
	batteries = СarBatteries.objects.order_by('brand', 'cranking_amps')
	brand = BrandName.objects.order_by('name')
	context = {
        'sitename': 'Интернет-магазин',
        'batteries': batteries,
        'brand': brand,
    }
	return render(request, 'batteries/index.html', context)

class AboutUs(TemplateView):
    template_name = 'batteries/about_us.html'

class Contacts(TemplateView):
    template_name = 'batteries/contacts.html'

'''
def  get_batteries(request):
	 brand = BrandName.objects.all()
	 
	pass

get_object_or_404(models.Category, slug=slug)
СarBatteries.objects.get(slug = slug)

def car_batteries_list(request):
	batteries = СarBatteries.objects.all()
'''	

def car_battery_detail(request, slug):
	battery = get_object_or_404(СarBatteries, slug=slug)
	context = {
        'sitename': 'Интернет-магазин',
        'battery': battery,
    }
	return render(request, 'batteries/battery.html', context)

