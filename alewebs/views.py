from django.shortcuts import render
from django.http import HttpResponseRedirect


def index(request):
    return render(request, 'alewebs/index.html')

def features(request):

	return render(request, 'alewebs/features.html')

def about(request):
	return render(request, 'alewebs/about.html')

def price(request):
	return render(request, 'alewebs/price.html')






