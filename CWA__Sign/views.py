from django.shortcuts import render

# Create your views here.

def Sign_In(request):
    return render(request, "sign/Sign_In.html")