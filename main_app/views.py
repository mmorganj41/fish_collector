from django.shortcuts import render, redirect
from .models import Fish, Toy
from .forms import FeedingForm
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic import ListView, DetailView

# Create your views here.

def add_feeding(request, fish_id):
	form = FeedingForm(request.POST)
	if form.is_valid():
		new_feeding = form.save(commit=False)
		new_feeding.fish_id = fish_id
		new_feeding.save()
	return redirect('detail', fish_id=fish_id)

def fish_detail(request, fish_id):
	f = Fish.objects.get(id=fish_id)
	# instantiate FeedingForm to be rendered in the template
	feeding_form = FeedingForm()
	toys_fish_doesnt_have = Toy.objects.exclude(id__in = f.toys.all().values_list('id')) 
	return render(request, 'fish/detail.html', {
    # include the f and feeding_form in the context
		'f': f, 'feeding_form': feeding_form, 'toys': toys_fish_doesnt_have
	})

class FishCreate(CreateView):
	model = Fish
	fields = ['name', 'species', 'description', 'age']

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

class ToyList(ListView):
	model = Toy

class ToyDetail(DetailView):
	model = Toy

class ToyCreate(CreateView):
	model = Toy
	fields = '__all__'

class ToyUpdate(UpdateView):
	model = Toy
	fields = ['name', 'color']

class ToyDelete(DeleteView):
	model = Toy
	success_url = '/toys/'
  
def assoc_toy(request, fish_id, toy_id):
	Fish.objects.get(id=fish_id).toys.add(toy_id)
	return redirect('detail', fish_id=fish_id)

def remove_toy(request, fish_id, toy_id):
	Fish.objects.get(id=fish_id).toys.remove(toy_id)
	return redirect('detail', fish_id=fish_id)