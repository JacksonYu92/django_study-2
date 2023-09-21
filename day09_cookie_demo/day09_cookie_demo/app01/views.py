from django.shortcuts import render, redirect, HttpResponse
from app01 import models

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    user = request.POST.get('user')
    pwd = request.POST.get('pwd')

    user_object = models.UserInfo.objects.filter(username=user,password=pwd).first()
    if user_object:
        # request.session["info"] = user_object.username
        request.session["info"] = {"name":user_object.username,"id":user_object.id}
        return redirect("/home/")
    else:
        return render(request, 'login.html', {'error': '用户名或密码错误'})

def home(request):
    # info_dict = request.session.get("info")
    info_dict = request.info_dict
    # if not info_dict:
    #     return redirect('/login/')
    return render(request, "home.html", {'info_dict': info_dict})

def order(request):
    # info_dict = request.session.get("info")
    # if not info_dict:
    #     return redirect('/login/')
    return render(request, 'order.html')