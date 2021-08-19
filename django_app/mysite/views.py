from django.shortcuts import HttpResponse, render

# Create your views here.
def display(request):
    return render(request, 'index.html')