from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def custom_404(request):
    return render(request, '404.html')

def custom_500(request):
    return render(request, '404.html')