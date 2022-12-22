from django.shortcuts import render
from .models import Fish
from django.views.generic.edit import DeleteView, UpdateView, CreateView

# Create your views here.

class FishCreate(CreateView):
	model = Fish
	fields = '__all__'

class FishUpdate(UpdateView):
	model = Fish
	fields = ['species', 'description', 'age']

class FishDelete(DeleteView):
	model = Fish
	success_url = '/fish/'


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