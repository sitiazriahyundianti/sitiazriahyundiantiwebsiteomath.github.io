from django.shortcuts import render

# Create your views here.
def rangkuman(request):
    return render(request, 'rangkuman.html')