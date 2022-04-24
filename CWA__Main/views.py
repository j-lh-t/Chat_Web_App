from django.shortcuts import render

# Create your views here.

#Todo: Đây là Trang chủ 
def index(request):
    return render(request,"main/index.html")