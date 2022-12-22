from django.shortcuts import render
from .models import Fish

# Create your views here.


def home(request):
	return render(request, 'home.html')

def about(request):
	return render(request, 'about.html')

def fish_index(request):
	fish = Fish.objects.all()
	return render(request, 'fish/index.html', {'fish': fish})

def fish_detail(request, f_id):
	f = Fish.objects.get(id=f_id)
	return render(request, 'fish/detail.html', {'f': f})