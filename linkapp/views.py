from django.shortcuts import render
from django.http  import HttpResponse,Http404
from django.shortcuts import render,redirect
from .models import Neighborhood,Profile,Business,Post


# Create your views here.
def index(request):
    neighborhoods = Neighborhood.get_all_neighborhoods()
    return render(request, 'index.html',{"neighborhoods":neighborhoods})