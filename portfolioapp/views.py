from django.shortcuts import render
from .models import about
# Create your views here.
def home(request):
    return render(request, 'blog/home.html')

def portfolio(request):
    return render(request, 'blog/portfolio.html')
    
def about_list(request):
    abouts = about.objects.all()
    stuff_for_fontend = {'abouts': abouts }
    return render(request, 'blog/about.html', stuff_for_fontend)
