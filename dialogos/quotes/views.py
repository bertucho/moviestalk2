from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from quotes.models import Quote, Movie
from random import randint

# Create your views here.
def index(request):
	quotes = Quote.objects.all()
	len = Quote.objects.count()
	N = randint(0,len-1)
	template = loader.get_template('../templates/base.html')
	return render(request,"../templates/base.html",{'quote':quotes[N]})

def getRandQuote():
	len = Quote.objects.count()
	print(len)
	query = SELECT text FROM mytable OFFSET random()*len LIMIT 1;