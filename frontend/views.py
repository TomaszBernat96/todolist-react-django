from django.shortcuts import render

# Create your views here.
def application_entry(request):
    return render(request, 'frontend/index.html')