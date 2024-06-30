from django.shortcuts import render

# Create your views here.

def home(requenst):
    return render(requenst, 'home.html', {})