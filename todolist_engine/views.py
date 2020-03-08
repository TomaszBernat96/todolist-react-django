from django.shortcuts import render

# Create your views here.

def application_view(request):
    return render(request, 'app/app.html')