from django.shortcuts import render, redirect
from .models import Fish
from .forms import FeedingForm
from django.views.generic.edit import DeleteView, UpdateView, CreateView

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
  return render(request, 'fish/detail.html', {
    # include the f and feeding_form in the context
    'f': f, 'feeding_form': feeding_form
  })

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
