from django.shortcuts import render

def index(request):
    return render(request,'education/index.html',)

# Create your views here.
