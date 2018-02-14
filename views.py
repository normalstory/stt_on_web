from django.shortcuts import render
# Create your views here.
def page_a(request):
    return render(request, 'pages/page_a.html',{}) 

def page_b(request):
    return render(request, 'pages/page_b.html',{}) 

def page_c(request):
    return render(request, 'pages/page_c.html',{}) 

def index(request):
    return render(request, './index.html',{})
