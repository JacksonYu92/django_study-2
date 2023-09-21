from django.shortcuts import render, redirect
from app01 import models

def user_list(request):
    queryset = models.User.objects.all()
    print(queryset)
    return render(request,'user_list.html', {'queryset':queryset})

def add_user(request):
    if request.method == "GET":
        depart_list = models.Department.objects.all()
        return render(request, 'add_user.html', {'depart_list':depart_list})

    user = request.POST.get("user")
    age = request.POST.get("age")
    salary = request.POST.get("salary")
    dp = request.POST.get("dp")

    models.User.objects.create(name=user, age=age, salary=salary, depart_id=dp)

    return redirect("/user/list/")