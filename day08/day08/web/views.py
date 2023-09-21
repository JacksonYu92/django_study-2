from django.shortcuts import render
from django.shortcuts import HttpResponse

def login(request):
    # return HttpResponse("登录页面")
    return render(request,'login.html')

def user_list(request):
    data = ['jackson', 'jack', 'jackie']

    mapping = {"name":"Jackson", "age": 20, "size": 23}

    return render(request, 'user_list.html', {"message":"标题来了", "data_list": data, "xx":mapping})

def phone_list(request):
    queryset = [
        {"id": 1,"phone": "1888888888", "city": "上海"},
        {"id": 2, "phone": "1888888883", "city": "北京"},
        {"id": 3, "phone": "1888888884", "city": "上海"},
        {"id": 4, "phone": "1888888885", "city": "上海"},
    ]

    return render(request, 'phone_list.html', {"data":queryset})