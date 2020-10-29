from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def landing_page(request):
    return render(request, 'landing.html')