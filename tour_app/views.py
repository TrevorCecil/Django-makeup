from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def product(request):
    return render(request,'product.html')

def form(request):
    return render(request,'form.html')