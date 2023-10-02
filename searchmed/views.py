from django.shortcuts import render

# Create your views here.
def home(request) :
	return render(request, 'searchmed/home.html', {})

def combine(request) :
    return render(request, 'searchmed/combine.html', {})