from django.shortcuts import render

# Create your views here.

#Todo: Đây là hàm trang Đăng nhập
def Sign_In(request):
    return render(request, "sign/Sign_In.html")