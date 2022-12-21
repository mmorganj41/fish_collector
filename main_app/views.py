from django.shortcuts import render

# Create your views here.

class Fish():
	def __init__(self, name, species, description, age):
		self.name = name
		self.species = species
		self.description = description
		self.age = age

fish = [
	Fish('Nemo', 'clownfish', 'adventurous mongrel', 0),
	Fish('Pokey', 'swordfish', 'loves to swordfight', 5),
	Fish('Fido', 'parrotfish', 'copies everything you say', 7),
]

def home(request):
	return render(request, 'home.html')

def about(request):
	return render(request, 'about.html')

def fish_index(request):
	return render(request, 'fish/index.html', {'fish': fish})