from django.shortcuts import render

# Create your views here.
def beranda(request):
    return render(request, 'beranda.html')
