from django.shortcuts import render
from django.http  import HttpResponse,Http404
from django.shortcuts import render,redirect
from .models import Neighborhood,Profile,Business,Post


# Create your views here.
def index(request):
    neighborhoods = Neighborhood.get_all_neighborhoods()
    return render(request, 'index.html',{"neighborhoods":neighborhoods})

def profile(request, username):
    title = "Profile"
    profile = User.objects.get(username=username)
    users = User.objects.get(username=username)

    businesses = Business.get_profile_bs(profile.id)
    posts = Post.get_profile_posts(profile.id)
    return render(request, 'profile.html', {'title':title,'profile':profile,'posts':posts, 'businesses':businesses})


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
