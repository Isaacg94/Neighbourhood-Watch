from django.shortcuts import render
from django.http  import HttpResponse,Http404
from django.shortcuts import render,redirect
from .models import Neighborhood,Profile,Business,Post


# Create your views here.
def index(request):
    neighborhoods = Neighborhood.get_all_neighborhoods()
    return render(request, 'index.html',{"neighborhoods":neighborhoods})

def my_area(request, id):
    title = "Neighborhood"
    neighborhood = Neighborhood.objects.get(id=id)

    return render(request, 'area.html', {'title':title,'neighborhood':neighborhood})

def join(request, id):
    current_user = request.user 
    neighborhood = Neighborhood.objects.get(id=id)
    neighborhood.occupants_count.add(current_user)
    neighborhood.save()
    return redirect("hood")
