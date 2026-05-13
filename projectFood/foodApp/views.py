from django.shortcuts import render
from .models import Car
from .models import Animal
from .models import Plant


    # Create your views here.
def landing(request):
        context = {'welcomeMessage': 'Welcome to the landing page!! '} # dict that will hold out data

        return render(request, 'foodApp/landing.html', context)

def home(request):
        cars = Car.objects.all
        animals = Animal.objects.all
        plants = Plant.objects.all

        context = {"cars": cars, "animals": animals, "plants": plants} # dict that will hold out data
        return render(request, 'foodApp/home.html', context)


def about(request):
        context = {'welcomeMessage': 'Welcome to the about page!! '} # dict that will hold out data
        return render(request, 'foodApp/about.html', context)

def contact(request):
        context = {'welcomeMessage': 'Welcome to the contacts page!! '} # dict that will hold out data
        return render(request, 'foodApp/contact.html', context)

def projects(request):
        context = {'welcomeMessage': 'Welcome to the projects page!! '} # dict that will hold out data
        return render(request, 'foodApp/projects.html', context)
        
